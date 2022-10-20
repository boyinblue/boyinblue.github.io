---
title: 파이썬에서 MP3 파일 비동기 재생 방법 (playsound async)
permalink: /004_python/007-python-playsound.html
description: 파이썬에서 MP3 파일 재생 방법과 playsound를 통해 비동기 재생 방식에 대해서 설명합니다.
category: python
---
### playsound 패키지


파이썬으로 MP3 파일을 재생하는 방법은 다양합니다. 
그 중에서도 <code>playsound</code> 패키지를 이용하면 
단 한 줄로 MP3 파일을 재생할 수 있습니다. 
(import 구문까지 포함하면 2 줄이면 충분합니다.) 


#### playsound 패키지 설치하기


<code>sudo pip3 install playsound</code> 명령으로 
<code>playsound</code> 패키지를 설치합니다. 


```bash
$ sudo pip3 install playsound
```


위와 같이 <code>playsound</code>를 설치하면 
아래 위치에 <code>playsound.py</code> 파일이 생성됩니다. 


```bash
$ ls /usr/local/lib/python3.9/dist-packages/playsound.py -all
-rw-r--r-- 1 root root 9466 Apr 15 20:33 /usr/local/lib/python3.9/dist-packages/playsound.py
```


#### playsound로 MP3 파일 재생하기


아래는 playsound로 MP3 파일을 재생하는 간단한 예제입니다. 


```python
import playsound

playsound.playsound("sample.mp3")
```


놀랍게도 한 줄로 mp3 파일을 재생시킬 수 있습니다. 
(import 구문까지 포함해도 2 줄로 재생이 가능합니다.) 


하지만 해당 함수는 치명적인(?) 단점을 가지고 있습니다. 
해당 함수는 파일 재생이 완료될 때까지 리턴을 하지 않기 때문에 
중간에 재생을 정지할 수도 없고, 재생이 끝날때까지 꼼짝없이 
기다리고 있어야 합니다. 


이 이유는 해당 함수가 동기화된 리턴 방식(syncronized return)으로 
동작하기 때문입니다. 
다른 표현으로 블로킹(blocking)이라고도 표현합니다. 


MP3 파일을 재생하는 도중에 다른 처리를 하기 위해서는 
playsound를 async 방식(non blocking 방식)으로 처리해야 합니다. 


#### playsound로 MP3 파일 재생하기 (ASYNC 방식)


playsound가 백그라운드(background)에서 동작하기 위해서는 
함수 호출시에 <code>non blocking</code> 옵션을 지정하면 됩니다. 


```python
import playsound
import time

playsound.playsound("sample.mp3", block=False)
time.sleep(5)
```

위의 <code>playsound.playsound("sample.mp3", block=False)</code> 구문은 
실행과 동시에 리턴이 됩니다. 


실행과 동시에 리턴이 되고, 파이썬 스크립트가 종료될 수 있기 때문에 
time.sleep(5)을 이용해서 MP3 파일 재생이 완료될 때까지 기다립니다. 


이번 예제를 통해서 백그라운드에서 MP3 파일을 재생시킬 수는 있지만, 
playsound는 치명적인(?) 단점을 가지고 있습니다. 


한 번 파일을 재생시키게 되면, 파일 재생을 정지시킬 방법이 없습니다. 
playsound는 MP3 파일 재생 이외의 제어는 전혀 불가능합니다. 


playsound 패키지에 포함된 <code>playsound.py</code> 파일을 살펴보면 
<code>playsound()</code> 메소드 이에외 어떤 함수도 없다는 것을 
확인하실 수 있습니다. 


#### playsound로 MP3 파일 재생하기 (Thread 방식)


비동기 방식으로 MP3 파일을 재생하는 또 다른 방법은 
쓰레드를 이용하는 방법입니다. 


```python
import playsound
import threading
import ctypes
import time

play_thread = None

def stop_mp3():
    global play_thread

    if not play_thread:
        return

    thread_id = None
    if hasattr(play_thread, '_thread_id'):
        thread_id = play_thead._thread_id
    else:
        for id, thread in threading._active.items():
            print("thread :", id, thread)
            if thread is play_thread:
                thread_id = id
                break

    print("Try to thread exit :", thread_id)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                    ctypes.py_object(SystemExit))
    if res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
        print('Exception raise failure')

def play_mp3(filename):
    global play_thread

    stop_mp3()

    play_thread = threading.Thread(target=playsound.playsound, 
                    args=(filename,), daemon=True)
    play_thread.start()

def main():
    while True:
        cmd = input("cmd :")
        play_mp3("sample.mp3")

if __name__ == '__main__':
    main()
```


위의 파이썬 스크립트는 MP3 파일 재생시에 쓰레드를 이용합니다. 


```python
play_thread = threading.Thread(target=playsound.playsound,
args=(filename,), daemon=True)
```


<code>threading.Thread()</code> 구문을 통해서 쓰레드를 생성하여 
MP3 파일을 재생하도록 하였습니다. 


또한, 재생 이전에 기존에 생성한 쓰레드가 있다면, 
기존 쓰레드를 종료시키는 코드가 포함되어 있습니다. 


하지만 이 역시도 제대로 동작하지 않습니다. 
그 이유는 Ubuntu Linux에서 playsound 패키지는 내부적으로 
<code>GStreamer</code>를 이용하는데, 
<code>Ctrl + C</code>를 입력해도 종료가 되지 않습니다. 


#### playsound로 MP3 파일 재생하기 (Thread 방식)
