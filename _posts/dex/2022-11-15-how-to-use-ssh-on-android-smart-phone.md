---
title: 안드로이드에서 ssh 쉘 실행시키는 방법 (Termius 앱 사용)
description: 갤럭시 스마트폰에서 제공하는 Dex에서 ssh 터미널을 사용하는 방법입니다. 
category: dex
tags: dex
image: https://user-images.githubusercontent.com/50429025/201841460-e9d2ef69-d658-4e58-bff2-1b75a49b4b65.jpg
---

삼성 갤럭시 S10 스마트폰을 2년 넘게 사용했다. 
그동안 DeX를 한 번도 사용할 기회가 없었다. 
최근 C-Type 멀티 허브를 구입해서 DeX를 사용해보니 무척 편리했다. 
내 스마트폰을 PC처럼 사용할 수 있는데 이 편리한 것을 왜 사용하지 않았나 싶다. 
지금도 모니터, 키보드, 마우스를 스마트폰에 연결해서 이 페이지를 작성하고 있다. 


C-Type 멀티허브 연결
---
삼성 DeX를 편리하게 사용하기 위해서는 C-Type 멀티허브를 구입해서 연결하는게 좋다. 
8포트짜리 멀티허브를 구입했는데 이더넷, HDMI, USB 3.0, C-Type, SD Card, Micro SD Card 등 포트들을 제공해서 편리했다. 
멀티 허브에 삼성 스마트폰을 연결하면 아래 화면처럼 DeX 화면이 뜬다. 
![Screenshot_20221115-112702_Samsung DeX Home.jpg](https://user-images.githubusercontent.com/50429025/201841400-4059a7e3-7d41-4c66-b36a-89f0c8267501.jpg)


Termius 설치
---
![Screenshot_20221115-141232_Google Play Store.jpg](https://user-images.githubusercontent.com/50429025/201841432-ca6e1200-8184-4c2d-812f-ed11e8c7a92f.jpg)
SSH 쉘을 이용해서 작업하는 것을 좋아한다. 
안드로이드 운영체제에서 SSH 쉘에 로그인할 수 있는 앱을 찾아봤다. 
몇가지 SSH 앱을 설치해서 사용해봤지만 Termius(터미어스) 앱이 가장 편리하다. 
앱스토어를 실행시켜서 `Termius`라는 프로그램을 설치하자. 


Termius 쉘 실행
---
![Screenshot_20221115-141302_Termius.jpg](https://user-images.githubusercontent.com/50429025/201841460-e9d2ef69-d658-4e58-bff2-1b75a49b4b65.jpg)
앱을 실행시키는 어렵지 않에 SSH 세션을 시작할 수 있다. 
속도도 빠르고 디자인도 마음에 든다.

Termius 단점
---
<kbd>Ctrl</kbd> + <kbd>C</kbd>와 <kbd>Ctrl</kbd> + <kbd>V</kbd> 기능이 동작하지 않아서 이게 제법 불편하다. 
<kbd>Ctrl</kbd> + <kbd>Insert </kbd>와 <kbd>Shift</kbd> + <kbd>Insert</kbd> 단축키도 시도해봤지만 동작하지 않았다. 
마우스 버튼을 이용해서 `복사하기`나 `붙여넣기`가 메뉴가 사용 가능한지 확인해봤으나 이 역시도 동작하지 않았다. 
