---
title: 우분투 리눅스에 서비스 등록하는 방법
description: 우분투 리눅스에 python 스크립트를 서비스로 등록하는 방법
---


우분투 리눅스에 서비스 등록하는 방법
===


우분투 리눅스가 시작되자마자 특정 프로그램 또는 스크립트가 
수행되도록 하는 방법은 여러가지가 있다. 


crontab을 이용해서 주기적으로 실행?
---


<code>crontab</code>에 등록해서 실행 여부를 확인한 이후에 
원하는 프로그램 또는 스크립트가 수행되지 않고 있다면 
백그라운드로 실행되도록 하는 방법이 있을 것이다. 



서비스 등록 방법
---


우선 관리자 권한으로 아래 경로에 파일을 생성합니다.


```bash
$ vi /etc/systemd/system/my.service
```


위의 파일에 아래와 같은 형식으로 입력하고 저장합니다. 


```
[Unit]
Description=Raspberry Pi Monitoring Service

[Service]
Type=simple
user=root
ExecStart=python3 service.py
ExecStop=pkill -f 'python3 service.py'
Restart=on-failure
RestartSec=60
WorkingDirectory=/home/boyinblue/project/raspberry/service

[Install]
WantedBy=multi-user.target
```


서비스 실행, 종료, 재시작 방법
---


### 서비스 실행 방법
 

```bash
$ sudo service raspberry_monitor start
```


### 서비스 종료 방법
 

```bash
$ sudo service raspberry_monitor stop
```


### 서비스 재시작 방법
 

```bash
$ sudo service raspberry_monitor restart
```


### 서비스 상태 확인 방법
 

```bash
$ sudo service raspberry_monitor status
```


주의할 점
---


서비스가 백그라운드로 자동으로 실행되기 때문에 
백그라운드로 실행시킬 필요는 없습니다. 


### 잘못된 예


```
ExecStart='python3 service.py &'
```


서비스는 자동으로 백그라운드로 실행되기 때문에 
<code>&</code>를 통해서 실행할 필요가 없습니다. 


오히려 이렇게 하게 되면 서비스가 제대로 시작되지 못하거나, 
서비스가 제대로 시작되었다는 정보를 확인할 수 없습니다. 


### 좋은 예


```
ExecStart=python3 service.py
```






[✔️  Ubuntu Linux에서 ssmtp로 이메일 전송하는 초간단 방법 (이메일 전송 자동화)](001.html 'ssmtp 패키지를 이용하여 이메일을 전송하는 방법에 ')
---


ssmtp 패키지를 이용하여 이메일을 전송하는 방법에 대해서 설명합니다.


[✔️  공인 IP를 확인하는 방법(Windows, Ubuntu Linux 공통)](002.html 'Ubuntu Linux 쉘에서 공인 IP를 확인하는 방')
---


Ubuntu Linux 쉘에서 공인 IP를 확인하는 방법을 설명합니다. 


[✔️  Ubuntu Linux Crontab 실행 안됨 (crontab에서는 bash 문법 허용 안됨)](003-ubuntu-crontab-does-not-work.html '우분투 리눅스에서 crontabl이 실행되지 않는 문제 해결 방법에 ')
---


우분투 리눅스에서 crontabl이 실행되지 않는 문제 해결 방법에 대해서 설명합니다.


[✔️  모질라 썬더버드 메일 설정 방법 (네이버, gmail, 다음, 네이트)](004-thunderbird-email-setting-naver-gmail-daum.html 'Ubuntu Linux에서 기본적으로 제공하는 메일 프로그램인 모질라 썬더버드에 개인 메일 계정을 연결하는 방법에 ')
---


Ubuntu Linux에서 기본적으로 제공하는 메일 프로그램인 모질라 썬더버드에 개인 메일 계정을 연결하는 방법에 대해서 설명합니다.


[✔️  dead.letter 파일의 정체 (삭제 요망)](005-what-is-dead_letteres.html 'Ubuntu Linux 파일 시스템에 생성되는 dead.letter 파일의 정체를 알아보고 어떻게 다뤄야 하는지에 대해')
---


Ubuntu Linux 파일 시스템에 생성되는 dead.letter 파일의 정체를 알아보고 어떻게 다뤄야 하는지에 대해서 알아보겠습니다.


[✔️  vim 띄워쓰기 설정 방법](007-how-to-vim-setting.html 'vim 패키지의 ')
---


vim 패키지의 띄워쓰기 설정 방법


[✔️  USB-to-Serial 장치를 연결했지만 /dev/tty/ttyUSB0 파일이 생성되지 않는 경우 조치 방법](008-usb-to-serial-no-ttyUSB0.html 'Ubuntu Linux 22.04에 USB-to-Serial 장치를 연결했지만 ttyUSB0 파일이 생성되지 않는 경우 조치하는 방법에 ')
---


Ubuntu Linux 22.04에 USB-to-Serial 장치를 연결했지만 ttyUSB0 파일이 생성되지 않는 경우 조치하는 방법에 대해서 설명합니다.


[✔️  우분투 리눅스에서 NetworkManager로 IP 설정 방법](009-ubuntu-network-manager-ip-setting.html '우분투 리눅스에서 IP를 설정하는 방법은 3가지가 있습니다. 그 중에서도 NetworkManager로 IP를 설정하는 방법에 ')
---


우분투 리눅스에서 IP를 설정하는 방법은 3가지가 있습니다. 그 중에서도 NetworkManager로 IP를 설정하는 방법에 대해서 설명합니다.


[✔️  색상 프로필을 만들려면 인증이 필요합니다.](010-ubuntu-xrdp-color-pkla.html 'XRDP 연결시 (색상 프로필을 만들려면 인증이 필요합니다.)라는 메시지가 반복적으로 표시')
---


XRDP 연결시 (색상 프로필을 만들려면 인증이 필요합니다.)라는 메시지가 반복적으로 표시될 경우 해결 방법


[✔️  Ubuntu Linux](index.html 'Ubuntu Linux에 대한 ')
---


Ubuntu Linux에 대한 내용을 기록합니다.
