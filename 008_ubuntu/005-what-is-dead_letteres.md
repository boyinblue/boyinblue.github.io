---
title: dead.letter 파일의 정체 (삭제 요망)
description: Ubuntu Linux 파일 시스템에 생성되는 dead.letter 파일의 정체를 알아보고 어떻게 다뤄야 하는지에 대해서 알아보겠습니다.
---


dead.letter 파일의 정체 (삭제 요망)
===


Ubuntu Linux 파일 시스템에 생성되는 dead.letter 파일의 정체를 알아보고 
어떻게 다뤄야 하는지에 대해서 알아보겠습니다.


dead.letter 파일의 정체는 무엇인가?
---


회사에서 Ubuntu Linux로 서버를 구축해서 잘 사용중입니다. 
퇴근 후 집에서는 라즈베리파이와 Note PC에 Ubuntu Linux를 설치해서 
나름 관심있는 분야에 대해서 공부도 하고, 웹서핑도 하는 편입니다.


어느날 회사 서버와 홈 서버에서 이상한 고용량 파일이 발견되기 시작합니다. 
파일명은 <code>dead.letter</code>입니다. 


```bash
$ ls -all dead.letter
-rw-rw-r-- 1 parksejin mail 40554601 Mar 23 06:30 dead.letter
```


용량은 무려 40MB나 됩니다. 
회사 서버에서는 훨씬 더 큰 용량도 목격한 적이 있습니다.


안에 어떤 내용이 들어있을지 너무 궁금해서 열어보기로 했습니다. 
vi로 해당 파일을 열어보니 메일 발송해 실패한 메시지들이 가득했습니다.


### dead.letter 파일의 일부 (#1. 실패한 crontab 메시지들)


```
/bin/sh: 1: pushd: not found
/bin/sh: 1: ./auto.sh: not found
/bin/sh: 1: popd: not found
```


dead.letter 파일을 열어보니 가장 먼저 보이는 것이 실패한 crontab 메시지들입니다. 
GitHub Pages의 sitemap과 README.md 파일들을 최신으로 만들어주는 작업을 
crontab에 등록해서 수행했습니다. 
crontab에서 pushd 명령을 수행할 수 없는 것도 모르고 사용했던 이력이 있는데요. 
제대로 동작이 안되었을 뿐만 아니라 불필요하게 dead.letter라는 파일에 실패 로그가 남고 있었던 것입니다.


### dead.letter 파일의 일부 (#2. 발송에 실패한 편지들)


```
<-] 220 smtp.gmail.com ESMTP - gsmtp
    36 [->] EHLO esregnet0409@gmail.com
    37 [<-] 501 5.5.4  https://support.google.com/mail/?p=helo - gsmtp
    38 ssmtp: Cannot open smtp.gmail.com:587
```


다음으로 목격되는 내용들은 발송에 실패한 메일들입니다. 
초기에 보내는 메일 서버 설정이 올바르지 않아서 
제대로 발송되지 않았던 이력이 있는데 그게 dead.letter에 쌓이고 있었던 것입니다.


결론
---


제 결론은요, 삭제가 답입니다. 
발송에 실패한 메일들 중에서 중요한 내용은 없어 보입니다. 


```bash
$ rm dead.letter
```


이상입니다. 


<!--001.html-->
[✔️  Ubuntu Linux에서 ssmtp로 이메일 전송하는 초간단 방법 (이메일 전송 자동화)](001.html)
---


ssmtp 패키지를 이용하여 이메일을 전송하는 방법에 대해서 설명합니다.


<!--002.html-->
[✔️  공인 IP를 확인하는 방법(Windows, Ubuntu Linux 공통)](002.html)
---


Ubuntu Linux 쉘에서 공인 IP를 확인하는 방법을 설명합니다. 


<!--003-ubuntu-crontab-does-not-work.html-->
[✔️  Ubuntu Linux Crontab 실행 안됨 (crontab에서는 bash 문법 허용 안됨)](003-ubuntu-crontab-does-not-work.html)
---


우분투 리눅스에서 crontabl이 실행되지 않는 문제 해결 방법에 대해서 설명합니다.


<!--004-thunderbird-email-setting-naver-gmail-daum.html-->
[✔️  모질라 썬더버드 메일 설정 방법 (네이버, gmail, 다음, 네이트)](004-thunderbird-email-setting-naver-gmail-daum.html)
---


Ubuntu Linux에서 기본적으로 제공하는 메일 프로그램인 모질라 썬더버드에 개인 메일 계정을 연결하는 방법에 대해서 설명합니다.


<!--006-ubuntu-register-serivce.html-->
[✔️  우분투 리눅스에 서비스 등록하는 방법](006-ubuntu-register-serivce.html)
---


우분투 리눅스에 python 스크립트를 서비스로 등록하는 방법


<!--007-how-to-vim-setting.html-->
[✔️  vim 띄워쓰기 설정 방법](007-how-to-vim-setting.html)
---


vim 패키지의 띄워쓰기 설정 방법


<!--008-usb-to-serial-no-ttyUSB0.html-->
[✔️  USB-to-Serial 장치를 연결했지만 /dev/tty/ttyUSB0 파일이 생성되지 않는 경우 조치 방법](008-usb-to-serial-no-ttyUSB0.html)
---


Ubuntu Linux 22.04에 USB-to-Serial 장치를 연결했지만 ttyUSB0 파일이 생성되지 않는 경우 조치하는 방법에 대해서 설명합니다.


<!--009-ubuntu-network-manager-ip-setting.html-->
[✔️  우분투 리눅스에서 NetworkManager로 IP 설정 방법](009-ubuntu-network-manager-ip-setting.html)
---


우분투 리눅스에서 IP를 설정하는 방법은 3가지가 있습니다. 그 중에서도 NetworkManager로 IP를 설정하는 방법에 대해서 설명합니다.


<!--010-ubuntu-xrdp-color-pkla.html-->
[✔️  색상 프로필을 만들려면 인증이 필요합니다.](010-ubuntu-xrdp-color-pkla.html)
---


XRDP 연결시 (색상 프로필을 만들려면 인증이 필요합니다.)라는 메시지가 반복적으로 표시될 경우 해결 방법


<!--_README.html-->
[✔️  Ubuntu Linux](_README.html)
---


Ubuntu Linux에 대한 내용을 기록합니다.


<!--index.html-->
[✔️  Ubuntu Linux](index.html)
---


Ubuntu Linux에 대한 내용을 기록합니다.


<!--001.html-->
[✔️  Ubuntu Linux에서 ssmtp로 이메일 전송하는 초간단 방법 (이메일 전송 자동화)](001.html)
---


ssmtp 패키지를 이용하여 이메일을 전송하는 방법에 대해서 설명합니다.


<!--002.html-->
[✔️  공인 IP를 확인하는 방법(Windows, Ubuntu Linux 공통)](002.html)
---


Ubuntu Linux 쉘에서 공인 IP를 확인하는 방법을 설명합니다. 


<!--003-ubuntu-crontab-does-not-work.html-->
[✔️  Ubuntu Linux Crontab 실행 안됨 (crontab에서는 bash 문법 허용 안됨)](003-ubuntu-crontab-does-not-work.html)
---


우분투 리눅스에서 crontabl이 실행되지 않는 문제 해결 방법에 대해서 설명합니다.


<!--004-thunderbird-email-setting-naver-gmail-daum.html-->
[✔️  모질라 썬더버드 메일 설정 방법 (네이버, gmail, 다음, 네이트)](004-thunderbird-email-setting-naver-gmail-daum.html)
---


Ubuntu Linux에서 기본적으로 제공하는 메일 프로그램인 모질라 썬더버드에 개인 메일 계정을 연결하는 방법에 대해서 설명합니다.


<!--006-ubuntu-register-serivce.html-->
[✔️  우분투 리눅스에 서비스 등록하는 방법](006-ubuntu-register-serivce.html)
---


우분투 리눅스에 python 스크립트를 서비스로 등록하는 방법


<!--007-how-to-vim-setting.html-->
[✔️  vim 띄워쓰기 설정 방법](007-how-to-vim-setting.html)
---


vim 패키지의 띄워쓰기 설정 방법


<!--008-usb-to-serial-no-ttyUSB0.html-->
[✔️  USB-to-Serial 장치를 연결했지만 /dev/tty/ttyUSB0 파일이 생성되지 않는 경우 조치 방법](008-usb-to-serial-no-ttyUSB0.html)
---


Ubuntu Linux 22.04에 USB-to-Serial 장치를 연결했지만 ttyUSB0 파일이 생성되지 않는 경우 조치하는 방법에 대해서 설명합니다.


<!--009-ubuntu-network-manager-ip-setting.html-->
[✔️  우분투 리눅스에서 NetworkManager로 IP 설정 방법](009-ubuntu-network-manager-ip-setting.html)
---


우분투 리눅스에서 IP를 설정하는 방법은 3가지가 있습니다. 그 중에서도 NetworkManager로 IP를 설정하는 방법에 대해서 설명합니다.


<!--010-ubuntu-xrdp-color-pkla.html-->
[✔️  색상 프로필을 만들려면 인증이 필요합니다.](010-ubuntu-xrdp-color-pkla.html)
---


XRDP 연결시 (색상 프로필을 만들려면 인증이 필요합니다.)라는 메시지가 반복적으로 표시될 경우 해결 방법


<!--_README.html-->
[✔️  Ubuntu Linux](_README.html)
---


Ubuntu Linux에 대한 내용을 기록합니다.


<!--index.html-->
[✔️  Ubuntu Linux](index.html)
---


Ubuntu Linux에 대한 내용을 기록합니다.


<!--001.html-->
[✔️  Ubuntu Linux에서 ssmtp로 이메일 전송하는 초간단 방법 (이메일 전송 자동화)](001.html)
---


ssmtp 패키지를 이용하여 이메일을 전송하는 방법에 대해서 설명합니다.


<!--002.html-->
[✔️  공인 IP를 확인하는 방법(Windows, Ubuntu Linux 공통)](002.html)
---


Ubuntu Linux 쉘에서 공인 IP를 확인하는 방법을 설명합니다. 


<!--003-ubuntu-crontab-does-not-work.html-->
[✔️  Ubuntu Linux Crontab 실행 안됨 (crontab에서는 bash 문법 허용 안됨)](003-ubuntu-crontab-does-not-work.html)
---


우분투 리눅스에서 crontabl이 실행되지 않는 문제 해결 방법에 대해서 설명합니다.


<!--004-thunderbird-email-setting-naver-gmail-daum.html-->
[✔️  모질라 썬더버드 메일 설정 방법 (네이버, gmail, 다음, 네이트)](004-thunderbird-email-setting-naver-gmail-daum.html)
---


Ubuntu Linux에서 기본적으로 제공하는 메일 프로그램인 모질라 썬더버드에 개인 메일 계정을 연결하는 방법에 대해서 설명합니다.


<!--006-ubuntu-register-serivce.html-->
[✔️  우분투 리눅스에 서비스 등록하는 방법](006-ubuntu-register-serivce.html)
---


우분투 리눅스에 python 스크립트를 서비스로 등록하는 방법


<!--007-how-to-vim-setting.html-->
[✔️  vim 띄워쓰기 설정 방법](007-how-to-vim-setting.html)
---


vim 패키지의 띄워쓰기 설정 방법


<!--008-usb-to-serial-no-ttyUSB0.html-->
[✔️  USB-to-Serial 장치를 연결했지만 /dev/tty/ttyUSB0 파일이 생성되지 않는 경우 조치 방법](008-usb-to-serial-no-ttyUSB0.html)
---


Ubuntu Linux 22.04에 USB-to-Serial 장치를 연결했지만 ttyUSB0 파일이 생성되지 않는 경우 조치하는 방법에 대해서 설명합니다.


<!--009-ubuntu-network-manager-ip-setting.html-->
[✔️  우분투 리눅스에서 NetworkManager로 IP 설정 방법](009-ubuntu-network-manager-ip-setting.html)
---


우분투 리눅스에서 IP를 설정하는 방법은 3가지가 있습니다. 그 중에서도 NetworkManager로 IP를 설정하는 방법에 대해서 설명합니다.


<!--010-ubuntu-xrdp-color-pkla.html-->
[✔️  색상 프로필을 만들려면 인증이 필요합니다.](010-ubuntu-xrdp-color-pkla.html)
---


XRDP 연결시 (색상 프로필을 만들려면 인증이 필요합니다.)라는 메시지가 반복적으로 표시될 경우 해결 방법


<!--_README.html-->
[✔️  Ubuntu Linux](_README.html)
---


Ubuntu Linux에 대한 내용을 기록합니다.


<!--index.html-->
[✔️  Ubuntu Linux](index.html)
---


Ubuntu Linux에 대한 내용을 기록합니다.
