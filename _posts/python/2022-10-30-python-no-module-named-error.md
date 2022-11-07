---
title: 파이썬 No module named 에러시 설치해야 할 모듈 정리
description: 파이썬 스크립트 실행시 No module named 에러시 설치해야 할 모듈 정리
category: python
image: /assets/images/python/logo.png
---
### 문제의 상황


No module named 에러
---

파이썬 스크립트 실행시에 "No module named"로 표시되는 에러는 필요한 모듈을 찾지 못해서 발생한다. 
pip3 명령으로 필요한 모듈을 설치하면 된다. 


`No module named 'speech_recognition'` 에러가 발생하면, 
SpeechRecognition 이라는 모듈을 설치해주면 된다. 


```bash
$ sudo pip3 install SpeechRecognition
```


### 에러별 설치해야 하는 모듈 리스트


|에러|설치해야 할 모듈|비고|
|---|---|---|
|No module named 'speech_recognition'|sudo pip3 install SpeechRecognition|  |
|No module named 'bs4'|sudo pip3 install beautifulsoup4|   |
|No module named 'tkinter'|sudo apt-get install python3-tk|   |


pip3: 명령이 없습니다 에러 발생할 경우
---


`pip3 install` 명령으로 모듈을 설치할 때, `pip3: 명령이 없습니다.` 발생하면 
`python3-pip` 패키지를 설치하면 된다. 


```bash
sudo apt-get install python3-pip
```

