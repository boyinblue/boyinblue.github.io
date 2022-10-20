---
title: 업비트 API 호출시에 "Too many API requests." 문제 해결 방법 3가지
permalink: /009_upbit/UPbit-Too-many-API-requests.html
description: 업비트 API 호출시에 "Too many API requests." 문제 발생시에 해결 방법에 대해서 설명합니다.
category: upbit
---


업비트 API 호출시에 "Too many API requests." 문제 해결 방법
===


이 페이지를 검색해서 열람하시는 분들이라면 
API와 업비트의 Open API에 대해서 익숙하신 분들이시겠지요. 


저는 매일 오전 9시 5분에 업비트 Open API를 이용해서 
일간 캔들 정보를 긁어와서 간단한 통계 자료를 만들고 있습니다. 


잘 동작하던 파이선 스크립트가 어제부터 아래와 같은 에러가 
발생하기 시작하더군요. 


```
Too many API requests.
```


다행히 제가 작성한 스크립트의 문제는 아니었습니다. 
모든 마켓의 캔들 정보를 연속으로 요청하다보니 
당연히 발생할 수 밖에 없는 상황입니다. 


사실 수많은 API가 Query(쿼리)의 개수나 순간 처리량 등을 제한하고 있습니다. 
꼭 API가 아니더라도 지메일(gmail) 같은 서비스 역시도 과도한 부하가 걸리지 않도록 쿼터제를 운영하고 있습니다. 


업비트 API의 요청 수 제한
---


업비트의 API 페이지에 가보면 API로 처리 가능한 요청 수 제한을 확인할 수 있습니다. 


[업비트 API](https://docs.upbit.com/docs/user-request-guide)


해당 페이지를 살펴보면 EXCHANGE API와 QUOTATION API에 대한 
요청수를 제한해 두었습니다. 


![업비트 API 요청 수]


초당 요청수와 분당 요청수가 제한되어 있는데, 
이 중에서 하나라도 초과하면 제대로된 응답을 받을 수 없습니다. 


다행히 과도한 쿼리에 대한 패널티는 없고, 
시간이 지나면 자동으로 해제가 됩니다. 


업비트 요청 수 제한 회피 방법 (첫번째)
---


우선 가장 먼저 단순하고 무식한 방법은 
쿼리와 쿼리 사이에 적당한 딜레이를 주는 것입니다. 


단순 조회용 API는 초당 10회까지 사용할 수 있으므로, 
쿼리마다 100ms의 딜레이를 주게되면 안정적으로 API를 처리할 수 있습니다. 


```python
# 마켓 목록을 market_code.json 파일에서 가져옴
with open("tmp/market_code.json") as json_file:
    json_data = json.load(json_file)
    for market_json_data in json_data:
        print(market_json_data)
        load_data_from_upbit(yesterday_date, market_json_data['market'])
        time.sleep(0.1)
```


기존 스크립트에는 딜레이 전혀 없이 처리를 했었는데, 
이번에는 <code>time.sleep(0.1)</code>을 넣어줬습니다. 


위와 같이 수행했더니 에러 없이 잘 처리가 되었습니다. 
하지만 이렇게 처리를 했을 경우에 의도하지 않은 문제가 발생할 수 있습니다. 


업비트 요청 수 제한 회피 방법 (두번째)
---


위와 같은 방법은 업비트에서 요청 수 처리 제한 정책이 바뀌면 
적당히 넣어준 딜레이 값을 다시 변경해줘야 되는 단점이 있습니다. 


예를들어서, 1분당 60개까지 요청할 수 있도록 되어 있었는데 
어느 순간 업비트에서 1분당 30개만 처리할 수 있도록 정책을 바꾼다면 
우리는 다시 또 "Too many API requests." 메시지를 맛보게 될 것이고 
적당히 딜레이를 더 넣어주는 작업을 또 해줘야 하기 때문입니다. 


손과 발이 편하자고 자동화를 하는데 조금이라도 수고로움을 줄여야 하겠지요. 
<code>try - exception 구문</code>을 사용해서 10번까지 재시도를 하도록 해보겠습니다. 


```python
# 마켓 목록을 market_code.json 파일에서 가져옴
from json.decoder import JSONDecodeError

with open("tmp/market_code.json") as json_file:
    json_data = json.load(json_file)
    for market_json_data in json_data:
        print(market_json_data)
        for trycnt in range(10):
            try:
                result = load_data_from_upbit(yesterday_date, market_json_data['market'])
                if result:
                    break
            except JSONDecodeError as e:
                print("JSODecodeError retry", trycnt)
                time.sleep(1)
                pass
            except Exception as e:
                raise e
```


<code>JSONDecodeError</code>를 처리하기 위해서는 
<code>json.decoder</code>를 import 시켜야 합니다. 


코드를 위와 같이 수정하면 요청 수 제한에 걸리기 전까지 
최대한 빠르게 API 호출이 처리됩니다. 


그러다가 요청 수 제한에 걸리게 되면 리턴되는 형식이 JSON이 아니라서 
JSONDecodeError가 발생하게 됩니다. 


이 때는 1초동안 쉬었다가 다시 retry를 하게 됩니다. 


업비트 요청 수 제한 회피 방법 (두번째)
---


마지막 3번째 방법을 웹소켓을 이용하는 방식입니다. 


해당 내용은 업비트 페이지 링크로 대신합니다. 


[업비트 웹소켓 관련 페이지](https://docs.upbit.com/docs/upbit-quotation-websocket)


결론
---


업비트 API 요청시에 "Too many API requests" 응답을 회피하는 방법에 대해서 알아보았습니다. 
