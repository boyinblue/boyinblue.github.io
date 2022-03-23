---
title: 업비트 API를 이용하여 일단위 캔들 조회 방법
description: 업비트에서 제공하는 Open API를 통해서 일단위 캔들을 조회하는 방법에 대해서 설명합니다.
---


업비트 API를 이용하여 일단위 캔들 조회 방법
===


기존 증권사의 API에 비해서 UPbit의 Open API는 아주 편리하게 되어 있습니다. 
캔들 조회는 토큰이 없어도 가능할 뿐만 아니라, 
JavaScript, Python, Ruby, Java 등 다양한 프로그래밍 언어를 이용해서 응용프로그램을 작성할 수 있도록 다양한 예제가 제공됩니다. 


본 페이지에서는 업비트 API 중에서도 가장 기본적인 기능인 <code>캔들 조회</code> 기능을 간단하게 구현해보고자 합니다.


본 페이지 작성 환경
---


이 페이지는 아래 환경을 기준으로 작성되었음을 미리 알려드립니다.
|OS|프로그래밍 언어|비고|
|--|--|--|
|Ubuntu Linux|Python, Curl||


업비트 Open API 관련 문서
---


업비트 Open API 관련 문서는 개발자 센터에서 열람하실 수 있습니다. 
[업비트 Open API 개발자 센터](https://docs.upbit.com)


서두에서도 설명드린 것처럼 다양한 언어로 레퍼런스 코드를 제공하기 때문에 
복사해서 붙여넣기로도 큰 어려움 없이 프로그램을 작성하실 수 있습니다.


curl 명령을 통한 시세 조회 (curl 명령)
---


우선 curl 명령을 통해서 캔들 정보를 받아와보겠습니다.
API를 통한 간단한 조회는 웹브라우저나 curl 명령으로도 충분히 수행 가능합니다. 
코드를 작성하거나 그런게 아니므로 처음부터 겁먹을 필요는 없습니다.


```bash
curl --request GET \
     --url 'https://api.upbit.com/v1/candles/days?count=1' \
     --header 'Accept: application/json'
```


위의 내용을 잘 살펴보면 일 단위(days)의 캔들(candles)들을 조회하는 명령이고, 
개수는 1개이므로 가장 최근의 캔들 1개만 요청하는 쿼리입니다. 
위의 같이 수행하면 아쉽게도 아래와 같은 에러가 발생합니다.


```
{"error":{"name":400,"message":"Missing request parameter error. Check the required parameters!"}}
```


분명 Open API를 위한 개발자 센터에서 제공된 예제인데, 
제대로 동작하지 않는다는게 좀 의아스러기도하고 아쉽기도 합니다.


아무래도 문서화 이후에 API쪽에 변경이 있었나 봅니다. 
API 관련된 필드 설명을 살펴보면 마켓 코드가 필수(mandotory)임을 알 수 있습니다. 
따라서 위의 쿼리에서 마켓 코드만 넣어주면 정상적으로 캔들 정보가 넘어옵니다.


```
curl –-request GET \
  --url 'https://api.upbit.com/v1/candles/days?count=1&market=KRW-BTC' \
  --header 'Accept: application/json'
```


위와 같이 URL에 조회를 원하는 마켓 정보를 <code>market=KRW-BTC</code>와 같이 추가로 실어주면 캔들 정보를 정상적으로 받아올 수 있습니다.


```json
[{"market":"KRW-BTC","candle_date_time_utc":"2022-03-23T00:00:00","candle_date_time_kst":"2022-03-23T09:00:00","opening_price":51689000.00000000,"high_price":51886000.00000000,"low_price":51300000.00000000,"trade_price":51465000.00000000,"timestamp":1648008580268,"candle_acc_trade_price":57777413849.17576000,"candle_acc_trade_volume":1119.60188760,"prev_closing_price":51704000.00000000,"change_price":-239000.00000000,"change_rate":-0.0046224663}]
```


출력 결과를 <code>jq '.'</code> 명령으로 예쁘게 찍어주면 아래와 같이 출력됩니다.


```json
[
  {
    "market": "KRW-BTC",
    "candle_date_time_utc": "2022-03-23T00:00:00",
    "candle_date_time_kst": "2022-03-23T09:00:00",
    "opening_price": 51689000,
    "high_price": 51886000,
    "low_price": 51300000,
    "trade_price": 51465000,
    "timestamp": 1648008580268,
    "candle_acc_trade_price": 57777413849.17576,
    "candle_acc_trade_volume": 1119.6018876,
    "prev_closing_price": 51704000,
    "change_price": -239000,
    "change_rate": -0.0046224663
  }
]
```


출력 결과중에서 시장가인 <code>trade\_price</code>를 보려면 <code>'jq .[trace\_price]'</code> 명령을 수행하면 됩니다.


```bash
curl –-request GET \
  --url 'https://api.upbit.com/v1/candles/days?count=1&market=KRW-BTC' \
  --header 'Accept: application/json' | jq '.[].trade_price'
```


아래와 같이 시장가만 깔끔하게 출력되게 됩니다.


```
51412000
```


curl 명령을 통한 시세 조회 (python)
---



