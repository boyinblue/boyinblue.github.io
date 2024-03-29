---
title: Git server certificate verification failed. CAfile none CRLfile none 에러 조치 방법
permalink: /001_github_api/003-server-certificate-verification-fail.html
description: GitHub 서버로부터 통신을 시도할 때 server certificate verification failed. CAfile none CRLfile none 에러가 발생할 경우 조치하는 방법에 대해서 설명합니다.
category: github-api
image: /assets/images/github-api/logo.png
---
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


{% assign preview_image_url = 'https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdI1EFK%2Fbtrb8gSuhde%2FCdMg8M1vbjjBv5mB54t8tK%2Fimg.png' %}
{% assign preview_url = 'https://frankler.tistory.com/64' %}
{% assign preview_title = '[라즈베리파이] 현재 시간 정보를 자동으로 가져와서 유지하는 방법' %}
{% assign preview_description = '라즈베리파이는
 현재 시간 정보를 유지하지 못합니다. 작고 저렴하지만 파워풀한 라즈베리파이에 RTC(Real Time Clock) 블록은 포함되어 있지 않습니다. 다시 말하면 라즈베리파이에는 현
재 시간 정보를 유지하는..' %}
{% include body-preview.html %}


이상입니다.
