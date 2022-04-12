---
title: 라즈베리파이4B에서 리모컨 입력 받아서 처리하는 방법 (Ubuntu 21.10)
description: 라즈베리파이4B에서 리모컨 입력 받아서 처리하는 방법 (Ubuntu 21.10)
---


라즈베리파이4B에서 리모컨 입력 받아서 처리하는 방법
===


라즈베리파이4B에서 리모컨 입력 받아서 처리하는 방법을 설명합니다. 
사실, 라즈베리파이를 이용해서 프로젝트를 진행하거나, 
스터디를 진행함에 있어서 가장 쉽게 접근할 수 있고, 
가장 손쉽게 정보를 얻을 수 있는 방법은 라즈비안을 사용하는 것입니다. 


하지만 제게 가장 익숙한 OS인 Ubuntu Linux를 포기할 수 없어서, 
라즈베리파이4B(rpi4)에 Ubuntu Linux 21.10을 설치했습니다. 


IR 센서를 이용해서 리모컨 입력을 받아서 처리하는 작업을 진행해보았습니다. 
대부분의 자료들이 라즈비안 베이스라서 Ubuntu Linux에서는 
어떻게 설정해야 하는지에 대한 정보를 얻기가 쉽지는 않았습니다. 


본 페이지에서는 Ubuntu Linux 21.10에서 VS 1838B IR 센서를 이용해서 
리모컨 입력을 받는 방법에 대해서 설명하고자 합니다. 


부디 여러분들이 찾는 도움이 되는 자료이기를 바랍니다.  


### 환경


|구분|세부 내용|비고|
|--|--|--|
|IR 센서|VS 1838B|   |
|H/W|Rpi4|   |
|OS|Ubuntu Linux 21.10|   |


OS 버전을 확인하려면 <code>lsb_release -a</code>를 입력하시면 됩니다. 


```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 21.10
Release:	21.10
Codename:	impish
```


제 RPi4에는 Ubuntu Linux 21.10이 설치되어 있습니다. 


### 하드웨어 연결


하드웨어 구성은 아주 간단합니다. 
<code>VS 1838B</code>라는 리모컨 수신 모듈은 
동작 전압이 3.3V이기 때문에 별도로 전압을 강하해줄 필요 없이 
라즈베리파이에 바로 연결이 가능합니다. 


VS 1838B를 정면에서 바라보았을 때, 
가장 왼쪽부터 <code>Output</code>, <code>GND</code>, <code>Vcc</code> 입니다.


|핀번호|신호|비고|
|--|--|--|
|1|Output|17번 핀에 연결|
|2|GND|   |
|3|Vcc|3.3V|


#### 회로 구성이 올바른지 확인 방법 #1


Output에 3.3V LED를 연결하면 리모컨 버튼을 눌렀을 때, 
LED가 아주 빠르게 깜빡거리는 것을 확인할 수 있습니다. 
그러면 회로 구성이 올바르게 되었다는 것을 알 수 있습니다. 


#### 회로 구성이 올바른지 확인 방법 #2


또한 회로 연결이 제대로 되었는지 확인하는 추가적인 방법은 
파이썬으로 GPIO17번 포트를 연속적으로 읽어보는 방법이 있습니다. 


이 때, 리모컨 버튼을 눌렀을 때 GPIO17번으로 읽은 입력이 변화한다면 
회로 연결이 제대로 구성되었다고 추측할 수 있겠습니다. 


### lirc 설치 및 설정


지금부터는 lirc 패키지를 설치하고, 설정 파일들을 편집해주는 작업입니다.


1. lirc 패키지 설치
2. /etc/lirc/lirc_options.conf 파일 편집
3. /boot/firmware/config.txt 파일 편집
4. ~~/etc/modules 파일 편집~~


#### lirc 패키지 설치


아래 명령으로 <code>lirc</code> 패키지를 설치합니다.


```bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install lirc
```


#### /etc/lirc/lirc_options.conf 파일 편집


아래 명령으로 <code>/etc/lirc/lirc_options.conf</code> 파일을 편집해줍니다.


```bash
$ sudo vi /etc/lirc/lirc_options.conf
```


파일 내용 중에 아래 2개 라인을 수정해줍니다. 


```
driver = default
device = /dev/lirc0
```


#### /boot/firmware/config.txt 파일 편집


아래 명령으로 <code>/boot/firmware/config.txt</code> 파일을 편집합니다. 


```
$ sudo vi /boot/firmware/config.txt
```


<code>dtoverlay=vc4-kms-v3d<code>로 되어 있는데 주석처리하고, 
<code>dtoverlay=gpio-ir,gpio_pin=17</code>를 추가로 입력해줍니다. 


어떤 기사를 보면 <code>/boot/config.txt</code> 파일을 편집하라고 하는데, 
Ubuntu 21.10 버전에서는 해당 파일이 없습니다. 


<code>/boot/config.txt</code> 파일이 아니라 
<code>/boot/firmware/config.txt</code> 파일을 편집하셔야 합니다. 


#### ~~/etc/modules 파일 편집~~~


어떤 기사를 보면 <code>/etc/modules</code> 파일을 편집하라는 내용이 있는데, 
제 경우는 이것이 오히려 부팅 불량을 야기하였습니다. 


아래와 같이 <code>/etc/modules</code> 파일을 편집한 이후로 
LED가 7번 깜빡거리면서 부팅하지 못하는 부팅 불량을 야기했습니다. 


이 때문에 이 설정을 원복(주석 처리)했더니 부팅이 정상적으로 이뤄졌습니다. 
또한, 이 파일을 편집하지 않았음에도 불구하고 동작에 전혀 문제가 없었습니다. 
특별한 경우가 아니라면 아래 과정을 생략하시기 바랍니다. 


아래 명령으로 <code>/etc/modules</code> 파일을 편집합니다. 


```
$ sudo vi /etc/modules
```


제 경우는 텅 비어있는데, 아래와 같이 2줄을 입력해줬습니다. 


```
lirc
lirc_rpi gpio_in_pin=17
```


### 재부팅 후 lirc 확인


재부팅 이후에 mode2 명령을 실행시킨 이후에 
리모컨을 눌러보면 아래와 같은 메시지가 출력됩니다.


```bash
$ sudo mode2 -d /dev/lirc0
Using driver default on device /dev/lirc0
Trying device: /dev/lirc0
Using device: /dev/lirc0
Running as regular user parksejin
pulse 224
timeout 130791
pulse 146
timeout 131392
pulse 146
```


결론
===


Ubuntu Linux 21.10이 설치된 라즈베리파이4B에 
IR 센서를 이용해서 리모컨 입력을 받는 방법에 대한 설명을 마칩니다. 



