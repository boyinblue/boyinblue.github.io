---
title: 색상 프로필을 만들려면 인증이 필요합니다.
description: XRDP 연결시 (색상 프로필을 만들려면 인증이 필요합니다.)라는 메시지가 반복적으로 표시될 경우 해결 방법
---


색상 프로필을 만들려면 인증이 필요합니다.
===


요약
---


### /etc/polkit-1/localauthority/50-local.d 디렉토리 생성


```
$ sudo mkdir -p /etc/polkit-1/localauthority/50-local.d
```


### /etc/polkit-1/localauthority/50-local.d/color.pkla 파일 편집


```
$ sudo vi /etc/polkit-1/localauthority/50-local.d/color.pkla
```


해당 파일에 아래 내용을 작성함.


```
[Allow colord for all users]
Identity=unix-user:*
Action=org.freedesktop.color-manager.create-device;org.freedesktop.color-manager.create-profile;org.freedesktop.color-manager.delete-device;org.freedesktop.color-manager.delete-profile;org.freedesktop.color-manager.modify-device;org.freedesktop.color-manager.modify-profile
ResultAny=yes
ResultInactive=yes
ResultActive=yes
```


혹은 wget으로 해당 파일을 다운로드 받아서 복사해도 됩니다.


```
$ wget https://raw.githubusercontent.com/boyinblue/test/main/ubuntu/color.pkla/color.pkla
$ sudo mv color.pkla /etc/polkit-1/localauthority/50-local.d/
```


### 관련 링크


[우분투 22.04에서 xrdp 연결시 색상 프로필을 만들려면 인증이 필요합니다. 라는 메시지가 뜨지 않도록 조치하는 방법](https://worldclassproduct.tistory.com/entry/%EC%9A%B0%EB%B6%84%ED%88%AC-2204-%EC%83%89%EC%83%81-%ED%94%84%EB%A1%9C%ED%95%84%EC%9D%84-%EB%A7%8C%EB%93%A4%EB%A0%A4%EB%A9%B4-%EC%9D%B8%EC%A6%9D%EC%9D%B4-%ED%95%84%EC%9A%94%ED%95%A9%EB%8B%88%EB%8B%A4-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95)


이상입니다


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


<!--005-what-is-dead_letteres.html-->
[✔️  dead.letter 파일의 정체 (삭제 요망)](005-what-is-dead_letteres.html)
---


Ubuntu Linux 파일 시스템에 생성되는 dead.letter 파일의 정체를 알아보고 어떻게 다뤄야 하는지에 대해서 알아보겠습니다.


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


<!--005-what-is-dead_letteres.html-->
[✔️  dead.letter 파일의 정체 (삭제 요망)](005-what-is-dead_letteres.html)
---


Ubuntu Linux 파일 시스템에 생성되는 dead.letter 파일의 정체를 알아보고 어떻게 다뤄야 하는지에 대해서 알아보겠습니다.


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


<!--005-what-is-dead_letteres.html-->
[✔️  dead.letter 파일의 정체 (삭제 요망)](005-what-is-dead_letteres.html)
---


Ubuntu Linux 파일 시스템에 생성되는 dead.letter 파일의 정체를 알아보고 어떻게 다뤄야 하는지에 대해서 알아보겠습니다.


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


<!--_README.html-->
[✔️  Ubuntu Linux](_README.html)
---


Ubuntu Linux에 대한 내용을 기록합니다.


<!--index.html-->
[✔️  Ubuntu Linux](index.html)
---


Ubuntu Linux에 대한 내용을 기록합니다.
