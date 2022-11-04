---
title: 파이썬 스크립트 실행시 No module named speech_recognition 에러가 발생했을 때 조치 방법
permalink: /004_python/006-python-no-module-speech-recognition.html
description: 파이썬 스크립트 실행시 No module named speech_recognition 이라는 에러가 발생했을 때 설치해야 하는 패키지명에 대해서 설명합니다. 
category: python
image: /assets/images/python/logo.png
---
### 문제의 상황


파이썬을 이용해서 TTS 기능을 하는 스크립트를 작성했습니다. 
다른 PC에서 해당 스크립트를 실행해보니 아래와 같은 에러가 발생했습니다. 


```
$ python3 tts.py 
Traceback (most recent call last):
  File "/project/tts/tts.py", line 1, in <module>
    import speech_recognition as sr
ModuleNotFoundError: No module named 'speech_recognition'
```


위의 문제는 <code>speech_recognition</code>이라는 모듈을 찾지 못해서 
발생한 문제입니다. 


### 해결 방법


해결 방법은 아주 간단합니다. 
<code>SpeechRecognition</code>이라는 패키지를 설치해주면 됩니다.


```bash
$ sudo pip3 install SpeechRecognition
```


모듈명이 <code>speech_recognition</code>라서 
<code>sudo pip3 install speech_recognition</code> 명령으로 
패키지를 설치하면 될 것 같지만 그렇지 않습니다. 


### 패키지 설치를 위한 스크립트 작성


모듈명과 설치해야 할 패키지 명이 상이하기 때문에 
파이썬 스크립트 배포시에 아래와 같이 패키지 설치를 위한 
스크립트를 같이 발행하는 것이 좋습니다. 


```bash
#!/bin/bash

sudo pip3 install SpeechRecognition
```


위와 같이 필요한 패키지를 설치할 수 있는 쉘 스크립트까지 같이 넣어준다면 
해당 파이썬 스크립트를 실행할 때 훨씬 더 편리하겠습니다. 


### 결론


파이썬 스크립트 실행시에 
<code>No module named 'spech_recognition'</code>이라는 에러가 발생했다면
<code>SpeechRecognition</code>이라는 패키지를 설치해주면 해결됩니다.


이상입니다.
