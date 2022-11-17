---
title: 파이썬 urllib.request시에 utf-8 code can't decode byte 에러 조치 방법 
description: Python에서 한글 인코딩 문제 해결 방법
category: python
image: /assets/images/python/logo.png
---

한글을 표시하는 방법은 여러가지가 있다. 
다양한 한글 코드가 존재하고, 인코딩 된 방식에 맞게 디코딩해야 한다. 
파일이나 URL로부터 읽은 데이터를 처리할 때 제대로 디코딩하지 못하면 텍스트가 깨지거나 예상하지 않은 오류가 발생한다. 
파이썬에서 한글 디코딩 문제가 발생할 때 해결할 수 있는 방법을 설명한다. 


디코딩 문제
---
아래의 파이썬 스크립에서 디코딩 에러가 발생했다. 

```python
import urllib.request
try:
  url = "https://boyinblue.github.io"
  req = urllib.request.Request(url)
  response = urllib.request.urlopen(url)
  print(response.read().decode('utf-8'))
except:
  print("Faild!")
```

위의 스크립트는 대부분의 웹페이지에서 문제 없이 동작했지만 특정 웹페이지에서는 에러가 발생했다. 

>utf-8 can't decode byte


문제의 해결
---
자주 사용하는 한글 코드를 리스트에 넣어놓고 시도하면 된다. 

```python
import urllib.request
try:
  url = "https://boyinblue.github.io"
  req = urllib.request.Request(url)
  response = urllib.request.urlopen(url)
  data = response.read()
  encodes = [ "utf-8", "euc-kr", "KSC5601", "cp949" ]
  for enc in encodes:
    try:
      print(data.decode(enc))
    except:
      print("Failed by {}".format(enc))
except:
  print("Faild!")
```

위의 스크립트는 'utf-8', 'euc-kr', 'KSC5601', 'cp949' 4가지 코드로 디코딩을 시도한다. 
현재까지 위의 방법으로 디코딩하지 못한 한글 문서나 웹페이지는 없었다. 
