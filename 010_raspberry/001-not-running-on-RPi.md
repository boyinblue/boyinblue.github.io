---
title: '라즈베리파이로 GPIO 제어시 \"RuntimeError: Not running on a RPi!\" 문제 해결 방법 (3가지)'
description: '파이선으로 작성한 GPIO 제어 스크립트가 "RuntimeError: Not running on a RPi!"라는 메시지와 함께 수행되지 못하는 문제를 해결하는 방법에 대해서 설명합니다.'
---


라즈베리파이로 GPIO 제어시 "RuntimeError: Not running on a RPi!" 문제 해결 방법 (3가지)
===


라즈베리파이로 가장 먼저 손쉽게 제어할 수 있는 것이 바로 GPIO 블록입니다. 
그 중에서도 GPO를 통해서 신호를 출력하는 방법은 단 몇 줄이면 충분합니다. 
아주 간단하게 LED를 켜거나 끌 수 있습니다.   


하지만 간혹 의도하지 않은 에러가 발생하기도 합니다. 
아주 간단한 실수임에도 불구하고, 그 원인을 어렵게 찾아내는 경우가 많습니다.
본 페이지에서는 "RuntimeError: Not running on a RPi!" 에러가 발생했을 때 시도해볼 수 있는 방법 3가지를 제공합니다.   


첫번째 방법 : 재부팅
---


제대로 동작하지 않을때 많이 시도해보는 방법입니다. 
좋은 방법은 아니지만 뛰어난 효과가 있을 때가 많습니다.


```bash
$ sudo reboot
```


두번째 방법 : 파이선 GPIO 패키지 설치
---


라즈베리파이를 처음 시작했거나, OS를 새로 설치했다면 패키지가 설치되지 않아서 발생하는 문제일 수 있습니다. 
아래의 명령을 통해서 파이선의 GPIO 패키지를 설치합니다.


```bash
$ sudo apt-get install python3-rpi.gpio
```


세번째 방법 : sudo 권한으로 파이선 스크립트 실행
---


GPIO를 제어하는 것은 관리자 권한이 필요합니다. 
이 때문에 GPIO를 제어하는 파이선 스크립트 실행시에 sudo를 입력하지 않으면 이런 에러가 발생할 수 있습니다. 
이 때는 아래와 같이 <code>sudo</code>를 추가하여 파이선 스크립트를 수행시켜주면 됩니다. 


```bash
$ sudo python3 gpio_control.py
```


결론
---


본 페이지에서는 라즈베리파이에서 "RuntimeError: Not running on a RPi!" 에러가 발생했을 때 조치할 수 있는 3가지 방법에 대해서 알아보았습니다.







[✔️  라즈베리파이4B에서 리모컨 입력 받아서 처리하는 방법 (Ubuntu 21.10)](002-rpi4-ir-receiver-ubuntu-21-10.html '라즈베리파이4B에서 리모컨 입력 받아서 처리하는 방법 (Ubu')
---


라즈베리파이4B에서 리모컨 입력 받아서 처리하는 방법 (Ubuntu 21.10)


[✔️  마이크로 서보 9G 모터 핀 번호 (라즈베리파이4B 서보 모터 제어 방법)](003-rpi4-servo-motor-control.html '마이크로 서보 9G 모터 핀 번호 및 라즈베리파이4B에서 서보 모')
---


마이크로 서보 9G 모터 핀 번호 및 라즈베리파이4B에서 서보 모터 제어 방법 설명


[✔️  Raspberry Pi](index.html '초소형 미니 컴퓨터인 라즈베리파이 관련 연구 ')
---


초소형 미니 컴퓨터인 라즈베리파이 관련 연구 내용을 정리합니다.


[✏️ ](https://www.github.com/boyinblue/boyinblue.github.io/edit/main/010_raspberry/001-not-running-on-RPi.md '수정하기')

