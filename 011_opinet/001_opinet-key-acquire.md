---
title: 오피넷 유가정보 API 무료 토큰 획득하는 방법
description: 대한석유공사가 운영중인 오피넷(Opinet)에서 제공하는 유가정보 API 토큰을 획득하는 방법에 대해서 설명합니다.
---


오피넷 유가정보 API 무료 토큰 획득하는 방법
===


대한석유공사가 운영중인 오피넷(Opinet)에서 제공하는 유가정보 API 토큰을 획득하는 방법에 대해서 설명합니다.


유가정보를 API로 수집하는 방법
---


Open API를 통해서 할 수 있는 것들을 무궁무진하게 많습니다. 
업비트와 같은 암호화폐 거래소에서 시세도 조회할 수 있고 자동 거래도 할 수 있고, 
대한석유공사에서 운영하는 오피넷이라는 서비스를 API를 통해 호출하면 유가 정보도 받아올 수 있습니다. 


유가정보 API 토큰 신청 방법
---


오피넷의 무료 API 토큰을 신청하려면 메일을 통해서 신청해야 합니다. 
price@knoc.co.kr 메일 주소로 메일을 보내면 됩니다. 
아래는 제가 토큰 신청시에 작성했던 메일 내용입니다.


```
제목 : 무료 API 이용 신청

안녕하세요?

무료 API 이용 신청 드립니다.
우선은 학습 목적이고, 추후에 어떻게 응용할 수 있을지 살펴볼 예정입니다.

감사합니다. 

OOO 드림
```

토요일에 신청했더니, 월요일에 회신이 왔습니다.


```
안녕하세요,

요청하신 무료 키 발급드립니다.

XXXXXXXXXX

감사합니다.
```

근데 10자리 키가 제법 허술하게 만들어진 것 같아요. 
<code>알파벳 하나</code> + <code>연월일(YYMMDD)</code> + <code>일련번호 3자리</code> 이런 형식이라는걸 누구든 쉽게 파악할 수 있겠더라고요. 


간단한 유가정보 조회 방법
---


아래의 스크립트를 이용하면 간단하게 전국 평균 유가를 검색할 수 있습니다. 


```bash
#!/bin/bash

KEY_CODE=$(cat token.txt)
URL="https://www.opinet.co.kr/api/avgAllPrice.do?out=json&code=${KEY_CODE}"
DATE=$(date "+%Y-%m-%d")
OUTPUT="tmp/${DATE}/oil_price.json"

mkdir -p tmp/${DATE}

echo "TOKEN : ${KEY_CODE}"

#curl --request GET \
#     --url "https://www.opinet.co.kr/api/avgAllPrice.do?out=json&code=${KEY_CODE}"

wget $URL -O ${OUTPUT}
```


토큰은 다른 API 호출시에도 사용될 수 있기 때문에 token.txt 파일에 저장해두었습니다. 
결과는 json 형식으로도 받을 수 있고, xml 형식으로도 받을 수 있습니다. 
저는 json이 편해서 json으로 쿼리를 보냈습니다. 
만약 xml로 수신하고자 하신다면 <code>out=xml</code>로 바꿔주시면 되겠습니다. 


API 요청이 정상적으로 처리되면 아래와 같은 응답이 옵니다. 


```
{
  "RESULT": {
    "OIL": [
      {
        "TRADE_DT": "20220324",
        "PRODCD": "B034",
        "PRODNM": "고급휘발유",
        "PRICE": "2216.32",
        "DIFF": "-0.75"
      },
      {
        "TRADE_DT": "20220324",
        "PRODCD": "B027",
        "PRODNM": "휘발유",
        "PRICE": "2001.90",
        "DIFF": "+0.18"
      },
      {
        "TRADE_DT": "20220324",
        "PRODCD": "D047",
        "PRODNM": "자동차용경유",
        "PRICE": "1919.09",
        "DIFF": "+0.84"
      },
      {
        "TRADE_DT": "20220324",
        "PRODCD": "C004",
        "PRODNM": "실내등유",
        "PRICE": "1411.08",
        "DIFF": "+2.31"
      },
      {
        "TRADE_DT": "20220324",
        "PRODCD": "K015",
        "PRODNM": "자동차용부탄",
        "PRICE": "1083.24",
        "DIFF": "+0.05"
      }
    ]
  }
}
```


출력 결과를 <code>jq</code>를 이용해서 좀 예쁘게 찍어봤습니다. 
러시아의 우크라이나 침공과 그에 따른 제재로 인해서 기름값이 정말 많이 올랐습니다. 


오피넷 유가정보 API 문서 (출처 : 오피넷)
---


[오피넷 유가정보 API 메뉴얼](Opinet_API_Free.pdf)


기타 다른 항목들은 위의 문서를 참고하시기 바랍니다. 
오피넷에서 다운로드 받았습니다. 


[오피넷 홈페이지](https://www.opinet.co.kr/searRgSelect.do#os_price3)


결론
---


오피넷 API의 토큰은 이메일로 신청해야하며, 
제 경우는 근무일 기준으로 1일만에 왔습니다. 




[✔️  OPINET API](index.html '대한석유공사의 오피넷에서 제공하는 Open API를 통해서 유가 동향 파악 및 통계 작성하는 ')
---


대한석유공사의 오피넷에서 제공하는 Open API를 통해서 유가 동향 파악 및 통계 작성하는 방법을 설명합니다.


[✏️ ](https://www.github.com/boyinblue/boyinblue.github.io/edit/main/011_opinet/001_opinet-key-acquire.md '수정하기')

