---
title: Ubuntu Linux에서 ssmtp로 이메일 전송하는 초간단 방법 (이메일 전송 자동화)
permalink: /008_ubuntu/001.html
description: ssmtp 패키지를 이용하여 이메일을 전송하는 방법에 대해서 설명합니다.
category: ubuntu
image: /assets/images/ubuntu/logo.png
---
많은 개발자들이 오해하고 있는 것이 있다. 
리눅스에서 메일을 송신하려면 SMTP 서버를 구축해야 되는지 말이다. 
구글에서 "Ubuntu 리눅스에서 메일을 보내는 방법"을 검색해보면 SMTP부터 구성하도록 작성된 글들이 많다. 
절대 그럴 필요 없다. 이 글이 여러분들의 시간과 노력을 절약해주기를 바란다.   

   
물론, 썬더버드(ThunderBird)와 같은 GUI 기반의 메일 송수신 프로그램을 제공하지만, 
그런 기본적인 내용을 다루는 글이라면 이 글을 시작하지도 않았을 것이다.   

   
이메일 전송 자동화를 이루려면 ssmtp처럼 쉘 명령으로 이메일을 전송할 수 있는 기능이 구현되어야 하기 때문이다. 
본 페이지에서는 ssmtp라는 프로그램으로 쉘에서 메일을 보낼 수 있는 방법을 소개한다.   

   
ssmtp 메일 전송 프로그램 소개
---

   
Ubuntu Linux에서는 ssmtp 프로그램을 이용하면 손쉽게 메일을 보낼 수 있다. 
SMTP 서버를 구성할 필요가 없고, gmail과 같은 메일 서비스를 그대로 이용할 수 있다. 
ssmtp라는 패키지를 설치하고 설정을 해주면 큰 어려움 없이 쉘 명령으로 메일을 전송할 수 있다.  
   

ssmtp의 가장 큰 단점이라면 첨부 파일을 보낼 수 없다는 것이다. 
만약 첨부파일 전송이 필요하다면 다른 종류의 메일 송신 프로그램을 사용하시기를 바란다. 

   
ssmtp 사용 방법
---

   
ssmtp로 메일을 송신하기 위해서는 아래와 같이 3단계가 필요하다.   

   
1. ssmtp 패키지를 설치해야 한다.
2. ssmtp 환경 설정이 필요하다. 
3. 형식에 맞는 메일 내용을 작성한 후에 ssmtp를 실행하면 된다.
   

ssmtp 패키지가 설치되어 있는지 확인하는 방법
---
   
ssmtp 패키지를 설치하는 방법을 설명하기에 앞서, 
ssmtp 패키지가 설치되어 있는지부터 먼저 확인해보겠다. 
쉘에서 아래 명령을 실행하고 그 결과를 확인해보자.   
   

```bash
$ ssmtp --version
```

   
만약 ssmtp가 설치되어 있다면 아래와 같은 결과가 나온다.   

   
```bash
ssmtp: No recipients supplied - mail will not be sent
```


만약 아래와 같은 결과가 나오면 ssmtp가 설치되어 있지 않으므로 설치해야 한다.   
   

```bash
명령어 'ssmtp' 을(를) 찾을 수 없습니다. 그러나 다음을 통해 설치할 수 있습니다:
sudo apt install ssmtp
```   


친절하게도 ssmtp를 사용하기 위해서는 설치해야하는 패키지까지 알려준다. 

   
ssmtp 패키지 설치 방법
---

   
ssmtp 패키지 설치하는 방법은 아주 간단하다. 
키를 추가하거나 소스 리스트를 추가해줄 필요도 없다. 
그저 쉘에서 아래 명령만 수행해주면 된다.   

   
```bash
$ sudo apt-get install ssmtp
```


ssmtp 환경 설정 방법 (gmail 기준)
---

   
그렇다면 지금부터는 gmail 기준으로 ssmtp 환경 설정하는 방법에 대해서 설명하겠다. 
결론부터 이야기하자면 아래와 같이 설정하면 된다.   

   
```bash
$ sudo vi /etc/ssmtp/ssmtp.conf
```

  
선호하는 편집기로 <code>/etc/ssmtp/ssmtp.conf</code> 설정 파일을 편집한다.   

   
아래와 같이 설정한다.   

   
```
root=yourmail@gmail.com
mailhub=smtp.gmail.com:587
FromLineOverride=YES
UseSTARTTLS=YES
UseTSL=YES
AuthUser=yourmail
AuthPass=app password (16자리 문자)
```

   
여기에서 주의할 것이 있다. 
AuthPass에 비밀번호를 입력하면 될 것 같지만, 실제로는 토큰을 입력해야 한다. 
앱 비밀번호를 입력해야 하는데, 이것은 계정 비밀 번호와는 다르다.   

   
관련 내용은 아래 사이트에 접속하면 앱 비밀번호 설정 방법에 대해서 확인할 수 있다.   


[gmail 앱 비밀번호 로그인](https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637831643180552872-3668500190&rd=1)

   
ssmtp로 간단하게 메일을 전송하는 방법
---

   
선호하는 편집기를 통해서 보낼 메일의 내용을 입력하면 된다. 
ssmtp로 메일을 보내기 위해서는 정해진 포맷의 헤더를 포함해야 한다. 

   
<pre><code>
To: boyinblue@hanmail.net
From: boyinblue: boyinblue@naver.com
MIME-Version: 1.0
Content-Type: text/html; charset=utf-8
Subject: This is a test mail
This is a test message.
</code></pre>

   
위와 같이 메일을 작성했다면 아래와 같이 명령어 한 줄로 메일을 전송할 수 있다. 

   
```bash
cat email.txt | ssmtp -v -t
```

   
<pre><code>
[<-] 220 smtp.gmail.com ESMTP **************************** - gsmtp
[->] EHLO parksejin-desktop
[<-] 250 SMTPUTF8
[->] STARTTLS
[<-] 220 2.0.0 Ready to start TLS
[->] EHLO parksejin-desktop
[<-] 250 SMTPUTF8
[->] AUTH LOGIN
[<-] 334 ******
[->] ******
[<-] 334 ******
[<-] 235 2.7.0 Accepted
[->] MAIL FROM:<boyinblue: esregnet0409@gmail.com>
[<-] 250 2.1.0 OK ******* - gsmtp
[->] RCPT TO:<boyinblue@hanmail.net>
[<-] 250 2.1.5 OK ******** - gsmtp
[->] DATA
[<-] 354  Go ahead *********** - gsmtp
[->] Received: by parksejin-desktop (sSMTP sendmail emulation); Fri, 18 Mar 2022 11:13:52 +0900
[->] Date: Fri, 18 Mar 2022 11:13:52 +0900
[->] To: boyinblue@hanmail.net
[->] From: boyinblue: esregnet0409@gmail.com
[->] MIME-Version: 1.0
[->] Content-Type: text/html; charset=utf-8
[->] Subject: This is a test mail
[->] This is a test message.
[->] 
[->] .
[<-] 250 2.0.0 OK  ******* - gsmtp
[->] QUIT
[<-] 221 2.0.0 closing connection ***** - gsmtp
</code></pre>

   
"ssmtp: Cannot open mail:25" 에러 발생시
---

   
만약 <code>ssmtp: Cannot open mail:25</code>라는 에러가 발생한다면, 
SMTP 서버 설정이 올바르지 않을 가능성이 있다. 
<code>/etc/ssmtp/ssmtp.conf</code> 파일을 열어서 mailhub 설정이 올바른지 확인해본다. 
   

```bash
$ sudo vi /etc/ssmtp/ssmtp.conf
```

   
<code>/etc/ssmtp/ssmtp.conf</code> 파일의 퍼미션은 0640이다. 
따라서 편집을 위해서는 root 권한이 필요하다. 
혹시라도 mailhub=mail 로 되어 있으면 mailhub에 SMTP 서버 주소를 기입한다. 

   
<code>mailhub=mail</code> 부분을 <code>mailhub=smtp.gmail.com</code>로 변경해준다.   

   
필자의 경우는 gmail을 예로 입력했지만, 그 외의 다른 SMTP 주소를 사용하면 된다.   

   
/etc/ssmtp/ssmtp.conf 파일을 편집하려고 하였으나 내용이 비어있을 경우
---

   
만약 <code>vi /etc/ssmtp/ssmtp.conf</code> 명령으로 파일 편집을 시도했는데, 
파일 내용이 완전히 비어있다면 퍼미션 문제이다.   

   
```bash
$ sudo ls -all /etc/ssmtp/ssmtp.conf
```

   
<code> sudo ls -all /etc/ssmtp/ssmtp.conf </code> 명령으로 해당 파일의 퍼미션을 삺펴보면 0640으로 되어 있는 것을 알 수 있다.   

   
```
-rw-r----- 1 root mail 598  3월 17 16:43 /etc/ssmtp/ssmtp.conf
```

   
즉, root만이 해당 파일을 편집할 수 있고, 읽기 권한은 mail 그룹만 가능하다. 
이 때는 <code>sudo</code> 명령을 통해서 root 권한으로 편집을 시도하면 된다.   

   
<code> sudo vi /etc/ssmtp/ssmtp.conf </code>와 같이 sudo 명령으로 파일 편집기를 열었는지 다시 확인해보자.   

   
"Must issue a STARTTLS command first" 에러 발생시
---

   
위와 같은 에러가 발생한다면 <code>ssmtp.conf</code> 파일을 열어서 <code>UseSTARTTLS=YES</code>와 같이 UseSTARTTLS 설정을 해주면 된다.   

   
```
root=esregnet0409@gmail.com
hostname=esregenet0409@gmail.com
FromLineOverride=YES
```


"ssmtp: Authorization failed (535 5.7.8)" 에러가 발생할 경우
---

   
아래와 같이 Authorization failed 에러가 발생했다면 앱 비밀번호가 올바르지 않다는 것이다. 
앞서 언급했듯이 AuthPass는 비밀번호가 아니라 앱 비밀번호이다.   

   
```
ssmtp: Authorization failed (535 5.7.8  https://support.google.com/mail/?p=BadCredentials j11-20020a63230b000000b00372a08b584asm6297113pgj.47 - gsmtp)
```

   
이 때는 앱 비밀번호를 발급받아서 AuthPass에 넣어주면 된다. 
앱 비밀번호는 16자리짜리 문자열이다.   

   
"도메인을 찾지 못하여 메일 전송이 안 되는 경우"
---

   
다음과 같은 DNS 오류가 발생한다면 hostname을 체크해보는게 좋다.   

   
```
주소를 찾을 수 없음

도메인을 찾지 못하여 abc@abc.com 주소로 메일을 전송하지 못했습니다. 
오타나 불필요한 공백이 있는지 확인한 후 다시 시도하세요. 

응답은 다음과 같습니다. 

DNS Error: DNS type 'mx' lookup of 'hostname' responded with code NXDOMAIN Domain name not found
```

   
이 때는 ssmtp.conf 설정 파일의 hostname을 체크해보시기 바란다.   
필자의 경우는 gmail 계정으로 ssmtp를 설정했고, 
hostname을 gmail의 smtp 서버 주소로 변경했더니 깔끔하게 문제가 해결되었다.   

   
기존에 잘못 입력된 hostname   

   
```
hostname=desktop
```

   
아래와 같이 hostname에 이메일의 smtp 주소를 입력해주면 된다.   

   
```
hostname=smtp.gmail.com:587
```

   
gmail 서비스에서 전송할 수 있는 할당량을 초과할 경우
---

   
아래와 같은 메시지가 발생하면서 메일이 전송되지 않는다면 
메일을 전송할 수 있는 할당량을 초과한 것이다.   

   
```
ssmtp: 550 5.4.5 Daily user sending quota exceeded. - gsmtp
```


gmail에서는 메일을 전송할 수 있는 할당량이 있다. 
[Gmail for Developers 문서](https://developers.google.com/gmail/api/reference/quota)


해당 문제는 일정 시간이 지나면 자동적으로 해결된다. 
참고로 특정 날짜 1일간에 보낼 수 있는 메일 개수가 제한된 것이 아니고, 
Average Moving 방식으로 쿼터제를 시행한다. 
혹시나 이런 문제가 자주 발생한다면 반복적으로 메일 발송을 과도하게 요청하고 있는것은 아닌지 체크하는게 좋다.


dead.letter라는 파일이 생성되어서 파일 크기가 점점 커짐
---


메일이 제대로 전송되지 못했을 경우 
dead.letter 파일에 전송되지 못한 메일 데이터가 계속 쌓이게 된다. 
메일 발송이 정말 중요해서 꼭 전달될 필요가 없다면 그냥 삭제하기를 권한다. 


[dead.letter 파일 정체](005-what-is-dead_letteres.html)

   
결론
---

   
이것으로 Ubuntu Linux에서 ssmtp 프로그램을 이용해서 메일을 전송하는 방법에 대한 설명을 모두 마친다.   
