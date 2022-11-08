---
title: 우분투 리눅스에서 단축키를 이용해서 프로그램을 실행시키는 방법
description: How to execute program with shortcut on Ubuntu linux
category: ubuntu
image: /assets/images/ubuntu/ubuntu-linux-short-cut-execute-4.png
---

단축키가 바로 치트키라고 생각합니다. 
어떤 작업이든 마우스를 이용하는 것보다 단축키를 사용하면 훨씬 더 빠르고 효율적입니다. 
우분투 리눅스에서 단축키를 이용해서 프로그램을 실행할 수 있습니다. 


요약
---

- 설정 -> 키보드 -> 바로 가기 보기 및 사용자 설정
- 키보드 바로 가기에서 바로 가기 사용자 설정
- 바로 가기 추가
- 사용자 설정 바로 가기 추가에서 이름, 명령, 바로 가기 추가
- 등록한 단축키로 프로그램이 실행되는 것을 확인


상세 설명
---

### 1. 바로 가기 보기 및 사용자 설정
![](/assets/images/ubuntu/ubuntu-linux-short-cut-execute.png)
설정 -> 키보드 -> 바로 가기 보기 및 사용자 설정 메뉴로 들어갑니다.

### 2. 바로 가기 사용자 설정 선택
![](/assets/images/ubuntu/ubuntu-linux-short-cut-execute-2.png)

### 3. 바로 가기 추가
![](/assets/images/ubuntu/ubuntu-linux-short-cut-execute-3.png)

### 이름, 명령을 입력
![](/assets/images/ubuntu/ubuntu-linux-short-cut-execute-4.png)

### 바로 가기 설정을 눌러 단축키 등록
![](/assets/images/ubuntu/ubuntu-linux-short-cut-execute-5.png)

### 단축키를 입력해서 테스트
![](/assets/images/ubuntu/ubuntu-linux-short-cut-execute-6.png)


제약 사항
---

우분투 리눅스에서 단축키로 프로그램을 실행하는데 몇가지 제약사항이 있습니다. 
이 점을 주의하시기 바랍니다. 

- GUI 프로그램만 가능
- 에러가 발생할 경우 확인이 어려움

### GUI 프로그램만 가능

CLI로 제작된 프로그램이나 스크립트는 실행이 불가능합니다. 
반드시 GUI로 화면이 뜨는 프로그램이나 스크립트만 실행이 가능합니다. 


### 에러가 발생할 경우 확인이 어려움

GUI로 화면이 뜨는 프로그램을 제작했더라도 프로그램 실행 도중 에러가 발생하면 원인을 확인하기 어렵습니다. 
예를 들어, 파이썬으로 tkinter를 이용해서 GUI로 프로그램을 제작했지만 실행 도중에 필요한 모듈을 찾지 못하는 경우가 발생할 수 있습니다. 
왜 프로그램이 실행되지 못했는지 확인이 어렵습니다. 


이 때는 해당 프로그램이나 스크립트를 쉘에서 실행해보면서 확인하면 됩니다. 

```
$ ./mkpv.py 
Traceback (most recent call last):
  File "/home/parksejin/project/mkpv/./mkpv.py", line 3, in <module>
    from tkinter import *
ModuleNotFoundError: No module named 'tkinter'

```

위와 같이 쉘에서 프로그래을 실행해보면, 왜 프로그램이 실행되지 못하는지 확인할 수 있습니다. 
제 경우는 파이썬 스크립트에서 사용하는 'tkinter'라는 모듈을 설치하지 않아서 발행한 문제였네요. 


팁
---

우분투 리눅스에서 단축키를 등록할 때 도움이 되는 팁들을 소개합니다. 

### 파이썬 스크립트 자동 실행하는 방법

파이썬 스크립트는 쉐뱅을 이용하면 실행 파일을 만들지 않아도 실행 가능합니다. 

{% assign preview_image_url = '"https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FclJgXB%2FbtrM5QDKJhh%2FJFx4VJXt9iUpQQbYKTms20%2Fimg.png"' %}
{% assign preview_url = 'https://worldclassproduct.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EC%9E%90%EB%8F%99%EC%8B%A4%ED%96%89-%EB%B0%A9%EB%B2%95-usrbinenv-python3' %}
{% assign preview_title = '"파이썬 스크립트 자동실행 방법 (#!/usr/bin/env python3)"' %}
{% assign preview_description = '"파이썬을 처음 시작했을 때는 파이썬 스크립트를 실행시킬 때마다 python 혹은 python3 명령을 붙여주었다. 하지만 파이썬에 어느 정도 익숙해진 지금은 shebang(셔뱅)을 이용해서 파이썬 스크립트를 자동으로 실행될 수 있도록 작성하고 있다. 셔뱅(shebang)이란? 셔뱅(shebang)이라는 것이 처음에는 조금 낯설 수 있겠다. 하지만 우리는 이미 습관적으로 셔뱅을 구사하고 있다. 우리가 bash script를 작성할 때 아주 습관적으로 가장 첫 번째 줄에 #!/bin/bash를 입력한다. 마찬가지로 파이썬 스크립트에 #!/usr/bin/env python3 구문을 입력하면 쉘은 알아서 python3를 실행하여 해당 스크립트를 수행한다. 배쉬 스크립트 셔뱅 예제 (script.sh) #!/bi.."' %}
{% include body-preview.html %}

### 단축키가 중복될 경우 다른 단축키 사용

![](/assets/images/ubuntu/ubuntu-linux-short-cut-execute-7.png)

만약 사용하려는 단축키가 이미 사용중이면 아래와 같이 다른 용도로 사용중이라는 것을 확인할 수 있습니다. 

><kbd>Alt</kbd>+<kbd>Print</kbd>은(는) 창의 스크린샷 찍기 용도로 사용 중입니다. 바꾸면 창의 스크린샷 찍기이(가) 사용 중지됩니다.

이 때는 다른 단축키로 변경해서 등록하면 됩니다. 