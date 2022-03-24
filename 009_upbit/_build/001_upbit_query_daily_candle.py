import requests
import json

# KRW-BTC 마켓의 오늘 코인 가격 하나만 조회하여 출력함.

url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&count=1"
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers)
#print(response.text)

st_python = json.loads(response.text)
print(st_python)
