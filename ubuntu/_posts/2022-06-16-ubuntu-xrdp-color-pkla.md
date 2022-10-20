---
title: 색상 프로필을 만들려면 인증이 필요합니다.
permalink: /008_ubuntu/010-ubuntu-xrdp-color-pkla.html
description: XRDP 연결시 (색상 프로필을 만들려면 인증이 필요합니다.)라는 메시지가 반복적으로 표시될 경우 해결 방법
category: ubuntu
---
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


[🔽 다음글 : 우분투 리눅스에서 NetworkManager로 IP 설정 방법](2022-05-11-ubuntu-network-manager-ip-setting.html '')
---



