---
title: 공인 IP를 확인하는 방법(Windows, Ubuntu Linux 공통)
permalink: /008_ubuntu/002.html
description: Ubuntu Linux 쉘에서 공인 IP를 확인하는 방법을 설명합니다. 
category: ubuntu
---


공인 IP를 확인하는 방법(Windows, Ubuntu Linux 공통)
===

   
네트워크에 대해서 잘 모르는 학부생 시절에 사설IP와 공인IP의 차이점에 대해서 잘 알지 못했다. 
학부생 시절 여름방학에 게임을 만드는 한 업체에서 현장실습을 할 기회가 있었는데, 
거기에서 공인IP와 사설IP의 차이점에 대해서 알 수 있었다.   

   
2000년 초반이었을 그 당시 그 게임 업체에서는 네트워크 게임을 개발 중이었는데, 
사설 IP를 이용해서 통신을 하다보니 제대로 접속이 되지 않는 문제로 많은 어려움을 겪었었나보다. 
지금이야 공인IP와 사설IP의 개념을 많은 사람들이 알고 있지만, 
그 당시에는 제법 고생하고 힘들게 알아냈던 정보였는지, 
현장 실습 인턴직이었던 나에게 공인IP와 사설IP에 대한 개념이 잘 정리된 문서를 
나에게 보여줬다.   

   
공인IP와 사설IP의 차이
---

   
공인IP(Public IP)라는 것은 전 세계에 주소가 단 하나뿐민 IP이다. 
해당 IP가 인터넷에 연결되어 있으면, 전 세계 어디서든 그 IP를 찾아낼 수 있다.   
 
  
IP 주소는 한정되어 있으므로 요즘에는 공인IP의 부족 사태를 겪고 있다. 
그래서 대안으로 나온 것이 IPV6이다.   

   
반면, 사설IP(Private IP)는 IP 대역 중에 일부를 사설 IP로 사용할 수 있도록 하였다. 
공인IP 하나에 인터넷 공유기를 연결하면 PC, 스마트폰 등의 단말기를 다양하게 사용할 수 있다. 이 때 사용하는 것이 바로, 사설 IP 대역이다. 
A, B, C 클래스의 일부를 사설 IP 대역으로 정해두었다. 
대표적으로 많이 쓰이는 대역은 B클래스의 192.168.0.0 ~ 192.168.255.255 대역이다.   


사설 IP는 당연히 중복될 수 있으며, 당연히 인터넷에서 라우팅이 불가능하다. 
그렇기 때문에 사설 IP를 가진 단말기가 인터넷에 접속하여 통신을 하기 위해서는 
공인 IP를 달고 통신을 해야 한다.   

   
공인IP를 확인하는 방법
---
  
 
컴퓨터의 IP를 확인하는 방법은 아주 간단하다. 
윈도우즈 PC의 경우는 <code>ipconfig</code> 명령을 실행해보면 된다. 
리눅스 PC는 <code>ifconfig</code> 명령을 실행해보면 된다.   

   
만약 리눅스 PC에서 ifconfig를 입력했을 때 IP가 표시되지 않는다면, 
아래의 명령으로 net-tools 패키지를 설치하면 된다.   

   
```bash
$ sudo apt-get install ifconfig
```

   
아마 대부분의 경우는 사설 IP 대역일 것이다. 
공인 IP를 바로 사용하는 회사, 학교 등을 제외하고는 사설 IP일 가능성이 아주 높다. 
만약, 가정에서 인터넷 공유기를 사용하지 않고 하나의 인터넷 회선을 바로 단말기에 연결해서 사용하는 경우라면 공인IP일 가능성이 높겠다.   

   
사설 IP가 할당된 단말기인데 공인IP를 어떻게 알 수 있을까? 
만약 인터넷 공유기를 사용하고 있다면, 인터넷 공유기 셋업 페이지에 접속해서 알아볼 수 있는 방법이 있다. 
대부분 게이트웨이 주소로 접속해보면 인터넷 공유기의 셋업 페이지에 접속할 수 있다. 
간혹 8080 포트로 접속해야 하는 경우도 있지만 대부분 큰 어려움 없이 접속해서 확인해볼 수 있다.   

   
공인IP를 확인하는 명령어
---

   
그럼 지금부터 공인IP를 확인하는 방법에 대해서 설명하겠다. 
인터넷 공유기에 접속하거나 그런 귀찮은 작업이 전혀 없이, 
오직 명령어 하나만 쉘에 입력하면 된다.   

   
<code> $ curl ifconfig.me </code>

   
위와 같이 입력하면 공인 IP 주소가 즉각적으로 떡하니 나온다. 

   
```
106.101.2.243
```

   
curl 명령은 리눅스와 윈도우즈 모두 사용할 수 있으므로 공통적으로 사용할 수 있다. 
만약, curl 패키지가 설치되어 있지 않으면 Ubuntu Linux 기준으로 아래의 명령을 입력하면 된다.   

   
```bash
$ sudo apt-get install curl
```

   
"curl ifconfig.me" 명령의 비밀!
---

   
curl 명령어는 인터넷에서 파일을 다운로드 받거나 받은 내용을 출력해주는 명령어다. 
그런 명령어에 ifconfig.me를 입력하면 공인IP를 알아낼 수 있는 옵션이 동작하는 것처럼 보일 수 있으나, 실제로는 그렇지 않다.   

   
curl 명령이 아니라 wget 명령으로도 공인IP를 알아낼 수 있다.   

   
```bash
wget ifconfig.me
cat index.html
```

   
눈치를 채셨는가? 
"ifconfig.me" 라는 것은 옵션이 아니올시다. 
웹서버 주소인 것이다.   

   
즉, <code>$ curl ifconfig.me</code>라는 명령은 아래의 명령과 equivalent 하다.   

   
```bash
$ curl http://ifconfig.me
$ curl https://ifconfig.me
```

   
그렇다. ifconfi.me는 웹서버 주소이기 때문에 웹서버에서 내 PC의 공인IP를 알려주는 것이다. 
웹 서버라는 것은 당연히 요청에 대한 응답을 제공해줘야 하는데, 
그럴려면 단말기의 공인 IP를 알고 있어야 한다.   

   
웹 브라우저로 열어보면 훨씬 더 많은 내용을 확인할 수 있다.   

   
![http://ifconfig.me](/assets/images/002-how-to-get-public-ip.png "What Is My IP Address? - ifconfig.me")

   
웹 페이지를 살펴보면 공인IP 외에도 더 많은 정보를 읽어올 수 있는 URL들을 제공한다.   

   
1. <code> curl ifconfig.me </code> : 공인IP를 받아 온다. 
2. <code> curl ifconfig.me/ip </code> : 위와 같은 동작이다. 
3. <code> curl ifconfig.me/ua </code> : 브라우저 정보를 읽어올 수 있다.
4. <code> curl ifconfig.me/lang </code> : 단말기의 언어를 알 수 있다.
5. <code> curl ifconfig.me/mime </code> : MIME 정보를 읽어올 수 있다.
6. <code> curl ifconfig.me/forwarded </code> 
7. <code> curl ifconfig.me/all </code> : 모든 정보를 받아올 수 있다.
8. <code> curl ifconfig.me/all.json </code> : 모든 정보를 json 포맷으로 받아올 수 있다.   

   
비슷한 서비스를 제공하는 웹서버(ifconfig.io)
---

   
비슷한 서비스를 제공하는 웹서버가 또 있다. 
바로 "https://ifconfig.io"이다. 
사용법은 ifconfig.if와 동일하다. 
쉘에서 아래와 같이 입력해주면 된다.   

   
```bash
$ curl ifconfig.io
```

   
결론
---

   
본 페이지에서 우리는 공인IP의 개념과 사설IP의 개념에 대해서 알아보았고, 
공인IP를 손쉽게 확인할 수 있는 방법에 대해서도 다뤄보았다. 
그리고 그 명령어의 의미가 어떻게 되는지에 대해서도 확인해보았다. 
비밀은, 공인IP를 알려주는 웹서버에 있었다.   
