---
title: 파이선 터틀 그래픽을 이용해서 간단한 랜덤 문자 출력 방법
permalink: /004_python/002.html
description: 파이선 터틀 그래픽을 이용하여 간단한 랜덤 문자를 출력하는 방법에 대해서 설명합니다.
category: python
---


파이선 터틀 그래픽을 이용해서 간단한 랜덤 문자 출력 방법
===

   
지난 시간에는 파이선의 opencv를 이용해서 이미지 파일을 출력하거나, 
웹캡 화면을 실시간으로 출력하는 방법에 대해서 알아보았습니다.   
   

이번 시간에는 파이선의 터틀 그래픽을 이용해서 간단한 문자 출력 방법에 대해서 설명을 드리고, 
간단한 예제를 보여드리도록 하겠습니다.   

   
(예제1) 화면에 a, b, c를 출력하세요.
---

   
우선 터틀 그래픽을 이용해서 간단한 랜덤 문자를 출력하는 방법입니다.   

   
```python
import turtle
import time

def main():

    turtle.setup(width=640, height=480)
    turtle.write("a", True)
    turtle.write("b", True)
    turtle.write("c", True)

    time.sleep(10)

if __name__ == '__main__':
    main()
```


전체 스크립트는 위와 같이 간단합니다. 
코드를 하나 하나씩 자세하게 설명드리겠습니다. 

   
```python
import turtle
```

   
터틀 그래픽을 이용하기 위해서 turtle 패키지를 import 시켰습니다.   

   
```python
import time
```

   
또한, 그래픽이 모두 그려진 이후에 10초간 화면이 표시될 수 있도록 하기 위해서 time 패키지를 import 시켰습니다.   
   

```python
turtle.setup(width=640, height=480)
```

   
main() 함수가 실행되면 화면의 크기를 가로 640, 세로 480 크기만큼 만듭니다. <code>setup()</code> 메소드는 터틀 그래픽이 그려진 화면의 크기를 설정합니다.   

   
```python
turtle.write("a", True)
turtle.write("b", True)
turtle.write("c", True)
```

   
이후에 "a", "b", "c" 문자를 순서대로 출력합니다. 
문자열을 터틀 그래픽에 출력하기 위해서는 <code>turtle.write(문자열, 커서 이동 여부)</code> 메소드를 사용하면 됩니다. 
두 번째 인자에 <code>True</code>를 입력하면 출력 후에 커서를 이동하고, <code>False</code>를 입력하면 출력 후에 커서 이동을 하지 않습니다.   

   
```python
time.sleep(10)
```

   
문자 출력이 완료되면 10초간 기다려서 그래픽 화면이 바로 닫히지 않도록 하였습니다. 

   
(예제2) 랜덤한 문자를 10개 1초에 하나씩 출력하는 예제
---

   
이번에는 랜덤한 문자 10개를 1초에 하나씩 출력하는 예제를 살펴보겠습니다.    

   
```python
import turtle
import time
import random

letters = [ "a", "b", "c", "d", "e", "f", "g" ]

def main():

    turtle.setup(width=640, height=480)

    cnt = 0
    while cnt < 10:
        rand_num = random.randrange(0, len(letters))
        turtle.write(letters[rand_num], True)
        time.sleep(1)
        cnt = cnt + 1

if __name__ == '__main__':
    main()
```

   
우선 import 시킨 패키지가 하나 추가되었습니다. 
바로 random 패키지입니다.   

   
```python
import random
```

   
출력할 문자의 리스트를 정의합니다.   
  
 
```python
letters = [ "a", "b", "c", "d", "e", "f", "g" ]
```

   
while 문을 이용해서 10회 반복을 합니다.   

   
```python
cnt = 0
while cnt < 10:
    # Todo Something
    time.sleep(1)
    cnt = cnt + 1
```

   
위의 while 문은 1초에 한번씩 <code># Todo Something</code>위치에 있는 코드를 수행할 것입니다.   

   
```python
rand_num = random.randrange(0, len(letters))
```

   
0부터 리스트의 개수만큼의 범위 안에서 랜덤값을 가져옵니다.    

   
위의 코드는 아래의 코드와 equivalent 합니다.   

   
```python
rand_num = random.randrand(0, 7)
```

   
letters 리스트의 개수가 추후에 변경될 수 있으므로 
리스트의 개수 만큼의 범위에서 가져올 수 있도록 하는게 좋습니다.   

   
```python
cnt = 0
while cnt < 10:
    rand_num = random.randrange(0, len(letters))
    turtle.write(letters[rand_num], True)
    time.sleep(1)
    cnt = cnt + 1
```

   
위와 같이 구현이 모두 완료되었습니다.   


관련 글
---


다음은 터틀 그래픽을 이용해서 여러가지 모양들을 그려보는 예제입니다. 


[파이썬 터틀 그래픽 재미있는 모양 예제](003-python-turtle-graphic-example.md)

   
결론
---

   
본 페이지에서는 터틀 그래픽과 랜덤을 이용해서 임의의 문자를 출력하는 예제에 대해서 설명드렸습니다.   
