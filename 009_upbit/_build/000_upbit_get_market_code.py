import requests
import json

# 목적 : 업비트의 마켓 코트를 가져옴
# 저장 : market_code.json 파일로 저장됨
output_file = "market_code.json"

# Query
url = "https://api.upbit.com/v1/market/all"
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers)
#print(response.text)

# Load json from response
st_python = json.loads(response.text)
#print(st_python)

# Write To File
with open( output_file, 'w' ) as fp:
    json.dump(st_python, fp)

