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




