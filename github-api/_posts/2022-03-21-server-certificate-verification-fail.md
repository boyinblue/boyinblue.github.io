---
title: server certificate verification failed. CAfile none CRLfile none 에러 조치 방법
permalink: /001_github_api/003-server-certificate-verification-fail.html
description: GitHub 서버로부터 통신을 시도할 때 server certificate verification failed. CAfile none CRLfile none 에러가 발생할 경우 조치하는 방법에 대해서 설명합니다.
category: github-api
---


[Git] "server certificate verification failed. CAfile: none CRLfile: none" 에러 조치 방법
===
   
필자는 초소형 컴퓨터인 라즈베리파이4B를 이용하여 본 웹페이지의 글을 작성하고 있다. 
라즈베리파이4B를 웹서버로 사용하는 것은 아니고, 
GitHub Pages라는 GitHub에서 제공하는 웹서비스를 이용해서 글들을 작성하고 있다.   
   
오늘 아침 Ubuntu Linux를 업그레이드하고 재부팅을 했더니, 
아래와 같은 메시지가 발생하면서 git에 접속을 할 수 없었다.   
   

문제 상황
---
   

git pull 명령을 수행하려 하였으나, 아래와 같은 메시지가 발생하면서 수행되지 않음.   
   

<pre><code>
fatal: unable to access 'https://github.com/boyinblue/boyinblue.github.io.git/': server certificate verification failed. CAfile: none CRLfile: none
</code></pre>
   

서버 인증서 검증에 실패했다는 이 메시지는 왜 발생을 했을까요? 
결론부터 이야기하자면, 재부팅 이후에 라즈베리파이의 RTC 값이 약 2개월 전으로 돌아갔기 때문입니다.   
   

문제 해결 방법 (현재 시간을 재설정)
---
   

문제를 해결하는 방법은 아주 간단합니다. 
라즈베리파이의 현재 시간을 재설정해주면 됩니다. 
라즈베리파이는 RTC 블럭을 제공하지만, RTC 값을 유지시켜주는 배터리가 없기 때문에, 
재부팅시에 현재 시간 설정이 올바르지 못한 경우가 있습니다. 
이 때문에 웹브라우저 접속이 안 되는 경우가 자주 발생합니다.   
   

RTC 값을 수동으로 설정해주는 것으로 본 문제를 해결할 수는 있었지만, 
이후에 재부팅될 경우 RTC 값이 맞지 않을 때마다 현재 시간을 매번 맞춰줘야 하는 것을 제법 성가신 일입니다.   
   

아래 페이지에는 라즈베리파이의 현재 시간 값을 자동으로 가져오는 방법에 대한 내용이 기술되어 있습니다.   


[링크 : 라즈베리파이 현재 시간 정보를 자동으로 가져와서 유지하는 방법](https://frankler.tistory.com/64)
   
   
이상입니다.   




[✔️  GitHub API 호출시 Bad Credentials 에러 발생시 조치 방법](001_bad_credential.html '본 페이지에서는 GitHub API 호출시에 Bad credentials 응답이 오는 문제를 해결하는 방법을 ')
---


본 페이지에서는 GitHub API 호출시에 Bad credentials 응답이 오는 문제를 해결하는 방법을 기술하고자 합니다.


[✔️  GitHub API .git-credentials 파일로부터 id와 token을 안전하게 파싱하는 방법](002_get_token_from_credential_file.html 'Bash 쉘 스크립트 및 파이썬 스크립트를 이용하여 GitHub 토큰를 파싱하는 ')
---


Bash 쉘 스크립트 및 파이썬 스크립트를 이용하여 GitHub 토큰를 파싱하는 방법을 설명합니다.


[✔️  GitHub에서 레포지토리의 생성일을 확인하는 방법](004-github-how-to-get-the-creation-date-of-repository.html 'GitHub API를 이용해서 레포지토리의 생성일을 확인하는 방법에 ')
---


GitHub API를 이용해서 레포지토리의 생성일을 확인하는 방법에 대해서 설명합니다.


[✔️  GitHub API](index.html 'GitHub API 사용 방법 및 관련')
---


GitHub API 사용 방법 및 관련 팁을 제공합니다.


[✏️ ](https://www.github.com/boyinblue/boyinblue.github.io/edit/main/001_github_api/003-server-certificate-verification-fail.md '수정하기')

