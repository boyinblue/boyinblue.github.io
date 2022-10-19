---
title: 파이썬 빈 배열 선언 방법
permalink: /004_python/009-python-how-to-declare-empty-array.html
description: 파이썬에서 빈 배열을 선언하는 방법에 대해서 설명합니다.
category: python
---


파이썬 빈 배열 선언 방법
===


파이썬에서 빈 배열을 선언하는 방법에 대해서 설명합니다. 


SW 개발자들은 평생 배워야 합니다. 
C, Bash Script, Python, PHP 등의 다양한 언어를 사용하다보면 
서로 다른 프로그래밍 문법을 혼동해서 사용하는 경우가 있습니다. 


C언어에서 배열 선언
---


예를들어, C 문법에서 배열을 선언하고자 한다면, 
<code>int array[10];</code> 구문으로 가능합니다. 


```C
int array[10];
```


Bash 스크립트에서 배열 선언
---


반면, Bash 쉘 스크립트에서는 아래의 구문으로 배열을 선언합니다. 


```bash
ARRAY=()
```


Bash 스크립트에서 연관 배열 선언
---


Bash 쉘 스크립트에서 연관 배열 선언하는 문법은 조금 다릅니다.


```bash
declare -A ASS_ARRAY
``` 


파이썬에서 배열 선언 (리스트 선언)
---


사실 파이썬에서 배열을 선언하는 명령은 없습니다. 
엄밀히 말하면 리스트를 선언한다고 표현을 해야 합니다. 
편의상 이 글에서는 '리스트' 대신 '배열'으로 지칭하겠습니다. 


```python
myList = []
```


파이썬에서 배열에 항목 추가
---


추가적으로 파이썬에서 배열에 항목을 추가하는 방법도 설명합니다. 


```python
myList = []

myList.append("https://boyinblue.github.io")
myList.append("https://blog.naver.com/boyinblue")
```


파이썬에서 배열의 크기 확인
---


파이썬에서 배열의 킄기를 확인하려면 <code>len()</code> 
함수를 사용하면 됩니다. 


```python
myList = []

myList.append("https://boyinblue.github.io")
myList.append("https://blog.naver.com/boyinblue")

print("배열 크기 :", len(myList))
```


파이썬에서 배열 순회하는 방법(#1)
---


파이썬에서 배열을 순회하는 방법은 여러가지가 있겠습니다. 
인덱스를 통해서 순회하는 방법이 있고, 그렇지 않은 방법이 있습니다. 


아래는 인덱스를 이용하지 않고 배열을 순회하는 방법입니다. 


```python
myList = []

myList.append("https://boyinblue.github.io")
myList.append("https://blog.naver.com/boyinblue")

for item in myList:
  print("URL : ", item)
```


파이썬에서 배열 순회하는 방법(#2)
---


명시적으로 항목 번호를 인덱싱하면서 탐색하는 방법입니다. 


```python
#!/usr/bin/env python3

myList = []

myList.append("https://boyinblue.github.io")
myList.append("https://blog.naver.com/boyinblue")

for id in range(len(myList)):
  print("URL[{}] : {}".format( id, myList[id]))
```


요약
---


✔️ 파이썬에서는 배열이 아니라 리스트라는 용어를 사용한다. 


✔️ 선언은 <code>myArray = []</code> 와 같이 하면 된다. 


✔️ 리스트의 크기를 확인하려면 <code>len(myList)</code>와 같은 
형식으로 작성하면 된다. 


이상입니다. 
