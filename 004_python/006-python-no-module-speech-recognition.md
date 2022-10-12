---
title: 파이썬 스크립트 실행시 No module named speech_recognition 에러가 발생했을 때 조치 방법
description: 파이썬 스크립트 실행시 No module named speech_recognition 이라는 에러가 발생했을 때 설치해야 하는 패키지명에 대해서 설명합니다. 
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






[✔️  OpenCV를 이용하여 이미지를 출력하는 방법과 캠을 동작시키는 방법](001.html 'OpenCV를 이용해서 이미지를 출력하는 방법과 실시간으로 캠 영상을 표시하는 방법에 대해')
---


OpenCV를 이용해서 이미지를 출력하는 방법과 실시간으로 캠 영상을 표시하는 방법에 대해서 설명합니다.  


[✔️  파이선 터틀 그래픽을 이용해서 간단한 랜덤 문자 출력 방법](002.html '파이선 터틀 그래픽을 이용하여 간단한 랜덤 문자를 출력하는 방법에 ')
---


파이선 터틀 그래픽을 이용하여 간단한 랜덤 문자를 출력하는 방법에 대해서 설명합니다.


[✔️  파이썬 터틀 그래픽 재미있는 모양 예제](003-python-turtle-graphic-example.html '파이썬 터틀 그래픽을 이용해서 원, 삼각형, 사각형, 입체 모양의 별, 꽃, 바퀴 등의 재미있는 모양을 그려보는 ')
---


파이썬 터틀 그래픽을 이용해서 원, 삼각형, 사각형, 입체 모양의 별, 꽃, 바퀴 등의 재미있는 모양을 그려보는 예제를 제공합니다.


[✔️  파이썬 명령행 인자 사용 방법](003-python-명령행인자.html '파이썬 스크립트 실행시에 명령행 인')
---


파이썬 스크립트 실행시에 명령행 인자를 추가하는 방법


[✔️  파이썬 vim 띄워쓰기 설정 방법](004-python-vim-setting.html 'vim을 이용하여 파이썬 스크립트 편집시에 ')
---


vim을 이용하여 파이썬 스크립트 편집시에 띄워쓰기 설정 방법


[✔️  파이썬 홈디렉토리 파일 오픈 방법](005-python-cannot-read-home-directory.html '파이썬에서 홈 디렉토리의 파일을 오픈하는 방법에 ')
---


파이썬에서 홈 디렉토리의 파일을 오픈하는 방법에 대해서 설명합니다.


[✔️  파이썬에서 MP3 파일 비동기 재생 방법 (playsound async)](007-python-playsound.html '파이썬에서 MP3 파일 재생 방법과 playsound를 통해 비동기 재생 방식에 ')
---


파이썬에서 MP3 파일 재생 방법과 playsound를 통해 비동기 재생 방식에 대해서 설명합니다.


[✔️  파이썬으로 워드프레스 글 자동 발행하기](008-python-wordpress-update.html '파이썬으로 워드프레스 글을 자동 발행하는 방법에 ')
---


파이썬으로 워드프레스 글을 자동 발행하는 방법에 대해서 설명합니다.


[✔️  Python](index.html 'Python 언어에 대한 내용을 기록')
---


Python 언어에 대한 내용을 기록하는 페이지입니다.
