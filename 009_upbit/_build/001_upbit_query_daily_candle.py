import requests
import json

url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&count=1"
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers)
#print(response.text)

st_python = json.loads(response.text)
print(st_python)
