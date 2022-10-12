---
title: [Git] 요청이 중단되었습니다. SSL/TLS 보안 채널을 만들 수 없습니다. (Visual Studio Code / Git 2.37.3)
description: Visual Studio Code에서 Git에 접근시에 요청이 중단되었습니다. SSL/TLS 보안 채널을 만들 수 없습니다. 에러가 발생할 때 조치하는 방법에 대해서 설명합니다.
---


[Git] 요청이 중단되었습니다. SSL/TLS 보안 채널을 만들 수 없습니다. (VS Code)
===


본 페이지에서는 Visual Studio Code에서 Git에 접근시에 
"요청이 중단되었습니다. SSL/TLS 보안 채널을 만들 수 없습니다."
라는 에러가 발생할 경우 조치하는 방법에 대해서 설명합니다. 


문제 발생 환경
---


윈도우즈 환경에서 Visual Studio Code 소스 편집기를 사용하고 있습니다. 
Git 버전은 2.37.3.windows.1 버전입니다.


|구분|내용|
|---|---|
|운영체제|Windows 11|
|편집툴|Visual Studio Code|
|Git 버전|2.37.3.windows.1|


문제의 상황
---


Visual Studio Code 터미널에서 git pull 명령을 수행시에 
인증 정보를 입력하여도, 
"요청이 중단되었습니다. SSL/TLS 보안 채널을 만들 수 없습니다."
라는 에러 메시지가 발생함.


문제의 해결
---


### 인증 정보를 설정한다.


```
> git config --global --add user.name (계정명)
> git config --global --add user.email (이메일 주소)
> git config --global --add credential.helper store
```


위와 같이 계정명, 이메일 주소를 설정하고, 
credential 정보를 로컬에 저장하도록 설정을 한다. 


### PowerShell에서 git pull 명령을 수행한다.


Visual Studio Code 터미널이 아닌 PowerShell에서 
해당 명령을 수행하면 정상적으로 처리가 된다. 


이상입니다. 


