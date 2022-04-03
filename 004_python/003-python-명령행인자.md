---
title: 파이썬 명령행 인자 사용 방법
description: 파이썬 스크립트 실행시에 명령행 인자를 추가하는 방법
---


title: 파이썬 명령행 인자 사용 방법
===


파이썬 스크립트에서 실행시 명령행 인자를 추가하는 방법에 대해서 설명한다.


명령행 인자가 왜 필요한가?
---


파이썬을 이용해서 조명을 제어하는 코드를 작성한다고 가정하자. 
조명 제어를 위한 아주 필수적인 메쏘드는 2가지이다. 


### 조명 제어를 위한 메쏘드


1. 조명을 켠다.
2. 조명을 끈다. 


위의 메쏘드를 실제로 라즈베리파이로 구현하면 아래와 같다. 


```python
import RPi.GPIO as GPIO

def light_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, False) #Low Active

def light_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, True) #Low Active
```


해당 스크립트 하나로 어떨때는 조명을 끄고, 
어떨때는 조명을 켜도록 하고 싶으면 어떻게 해야 할까? 


우선 먼저 어떤 동작을 할지에 대한 내용을 
표준입력(사용자 키보드 입력)으로 받아서 처리하는 방법이 있겠다.


### 표준 입력을 통한 처리


```python
def main():
    while True:
        cmd = input("cmd : ")
        if cmd.lower() == "on":
            light_on()
        elif cmd.lower() == "off":
            light_off()
        else:
            print("Unknown Command")

if __name__ == '__main__':
    main()
```


위의 스크립트는 <code>input</code> 함수를 통해서 
표준입력(키보드)로 받은 문자열로 전등을 켤 수도 있고, 
반대로 전등을 끌 수도 있다. 


```
$ sudo python3 light.py
cmd : on
cmd : off
```


<code>on</code>을 입력하면 전등이 실제로 켜지고, 
<code>off</code>를 입력하면 전등이 실제로 꺼진다. 


일단 잘 동작하는 것 같지만 한 가지 문제가 있다. 
표준 입력 없이는 어떠한 동작도 할 수 없다는 것이다. 


만약 위의 파이썬 스크립트를 <code>crontab</code>이나 
<code>bash</code> 스크립트에서 호출하고자 한다면 
표준 출력을 다시 표준 입력으로 넣어주는 번거로움이 있다. 


만약 오전 6시마다 crontab이 전등을 켜도록 하고, 
저녁 9시마다 crontab이 전등을 끄게 하려면 
아래와 같이 다소 깔끔하지 못한 명령을 입력해야 한다. 


```
$ echo on | sudo python3 light.py
```


<code>light.py</code> 파일이 표준 입력으로 제어 명령을 받기 때문에 
표준 출력으로 <code>"on"</code>을 출력하고, 파이프를 통해서 
표준 출력을 다시 <code>sudo python3 light.py</code>의 
표준 입력으로 넣어주는 트릭(?)을 쓸 수밖에 없다.


명령행 인자 사용
---


위와 같이 표준 입력을 통해서 사용자의 입력을 받아서 처리하는 방법도 있겠지만 
스크립트 실행 시점에 어떤 동작을 할지를 인자로 넣어주는 방법이 훨씬 깔끔하다. 







