---
title: USB-to-Serial 장치를 연결했지만 /dev/tty/ttyUSB0 파일이 생성되지 않는 경우 조치 방법
description: Ubuntu Linux 22.04에 USB-to-Serial 장치를 연결했지만 ttyUSB0 파일이 생성되지 않는 경우 조치하는 방법에 대해서 설명합니다.
---


ttyUSB0 파일이 생성되지 않는 문제 해결 방법
===


리눅스 PC에 <code>USB-to-Serial</code> 케이블을 연결하면 자동으로 
<code>/dev/ttyUSB0</code>와 같은 장치 파일일 생성되어야 합니다. 


만약, 여러개의 USB-to-Serial 케이블을 연결했다면, 
<code>/dev/ttyUSB0</code>, <code>/dev/ttyUSB1</code> 등 
여러개의 장치 파일이 생성되어야 합니다.


하지만 최근 Ubuntu Linux 22.04로 업그레이드한 이후부터는 
USB-to-Serial 케이블을 연결해도 /dev/ttyUSB0와 같은 파일들이 
제대로 생성되지 못하는 문제가 목격되고 있습니다. 


정확히 이야기하자면, /dev/ttyUSB0 파일이 생성되었다가, 
금새 사라진다는 것이 좀 더 정확한 표현입니다. 


이 문제를 정의하고 해결하는 방법에 대해서 설명을 드리고자 합니다. 


문제의 현상
---


문제를 정확히 정의하고 원인을 찾아야 정확한 해결이 가능합니다. 


<code>lsusb</code>명령을 통해서 인식된 USB 장치들을 확인합니다.


```bash
$ lsusb
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 007: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
Bus 001 Device 008: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
Bus 001 Device 003: ID 03f0:1b4a HP, Inc HP Wireless Slim Keyboard - Skylab KR
Bus 001 Device 006: ID 03f0:f92a HP, Inc HP Color LaserJet MFP E785
Bus 001 Device 002: ID 2109:3431 VIA Labs, Inc. Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```


아래와 같이 USB-to-Serial 장치가 정상적으로 인식된 것을 확인할 수 있습니다. 


```
Bus 001 Device 007: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
Bus 001 Device 008: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
```


<code>$ sudo udevadm monitor -u</code> 명령으로 인식 로그를 살펴봅니다. 


```bash
sudo udevadm monitor -u
monitor will print the received events for:
UDEV - the event which udev sends out after rule processing

UDEV  [82546.546942] add      /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4 (usb)
UDEV  [82546.563176] add      /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0 (usb)
UDEV  [82546.585015] add      /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/gpiochip2 (gpio)
UDEV  [82546.585142] add      /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/gpio/gpiochip500 (gpio)
UDEV  [82546.591547] add      /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/ttyUSB0 (usb-serial)
UDEV  [82546.593562] bind     /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/gpiochip2 (gpio)
UDEV  [82546.645324] add      /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/ttyUSB0/tty/ttyUSB0 (tty)
UDEV  [82546.664143] bind     /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/ttyUSB0 (usb-serial)
UDEV  [82546.671965] bind     /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0 (usb)
UDEV  [82546.692266] bind     /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4 (usb)
UDEV  [82549.950939] remove   /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/gpio/gpiochip500 (gpio)
UDEV  [82549.951788] remove   /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/ttyUSB0/tty/ttyUSB0 (tty)
UDEV  [82549.953358] unbind   /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/gpiochip2 (gpio)
UDEV  [82549.959662] unbind   /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/ttyUSB0 (usb-serial)
UDEV  [82549.960285] remove   /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/gpiochip2 (gpio)
UDEV  [82549.965710] remove   /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/ttyUSB0 (usb-serial)
UDEV  [82549.974262] unbind   /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0 (usb)
```


로그를 잘 살펴보면 ttyUSB0로 add되고 bind된 이후에, 
unbind되고 remove 된 것을 알 수 있습니다. 


```
UDEV  [82546.645324] add      /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/ttyUSB0/tty/ttyUSB0 (tty)
```


```
UDEV  [82546.664143] bind     /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/ttyUSB0 (usb-serial)
```


```
UDEV  [82549.959662] unbind   /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/ttyUSB0 (usb-serial)
```


```
UDEV  [82549.965710] remove   /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/ttyUSB0 (usb-serial)
```


해결 방법
---


<code>/usr/lib/udev/rules.d/85-brltty.rules</code> 파일을 열어서 
USB-to-Serial로 인식된 코드를 주석 처리 합니다. 


### 기존 설정


```bash
$ sudo vi /usr/lib/udev/rules.d/85-brltty.rules
# Device: 0403:6001
# Generic Identifier
# Vendor: Future Technology Devices International, Ltd
# Product: FT232 USB-Serial (UART) IC
# Albatross [all models]
# Cebra [all models]
# HIMS [Sync Braille]
# HandyTech [FTDI chip]
# Hedo [MobilLine]
# MDV [all models]
ENV{PRODUCT}=="403/6001/*", ATTRS{manufacturer}=="FTDI", ENV{BRLTTY_BRAILLE_DRIVER}="hd,hm,ht", GOTO="brltty_usb_run"
ENV{PRODUCT}=="403/6001/*", ATTRS{manufacturer}=="Hedo Reha Technik GmbH", ENV{BRLTTY_BRAILLE_DRIVER}="hd,hm,ht", GOTO="brltty_usb_run"
```


아래 라인들을 주석 처리합니다.


```
ENV{PRODUCT}=="403/6001/*", ATTRS{manufacturer}=="FTDI", ENV{BRLTTY_BRAILLE_DRIVER}="hd,hm,ht", GOTO="brltty_usb_run"
ENV{PRODUCT}=="403/6001/*", ATTRS{manufacturer}=="Hedo Reha Technik GmbH", ENV{BRLTTY_BRAILLE_DRIVER}="hd,hm,ht", GOTO="brltty_usb_run"
```


### 새 설정


```bash
$ sudo vi /usr/lib/udev/rules.d/85-brltty.rules
# Device: 0403:6001
# Generic Identifier
# Vendor: Future Technology Devices International, Ltd
# Product: FT232 USB-Serial (UART) IC
# Albatross [all models]
# Cebra [all models]
# HIMS [Sync Braille]
# HandyTech [FTDI chip]
# Hedo [MobilLine]
# MDV [all models]
#ENV{PRODUCT}=="403/6001/*", ATTRS{manufacturer}=="FTDI", ENV{BRLTTY_BRAILLE_DRIVER}="hd,hm,ht", GOTO="brltty_usb_run"
#ENV{PRODUCT}=="403/6001/*", ATTRS{manufacturer}=="Hedo Reha Technik GmbH", ENV{BRLTTY_BRAILLE_DRIVER}="hd,hm,ht", GOTO="brltty_usb_run"
```


시스템을 재부팅합니다. 


```bash
$ sudo reboot
```


재부팅후에 USB-to-Serial 케이블이 제대로 인식되었는지 살펴봅니다. 


```bash
$ ls /dev/ttyUSB*
/dev/ttyUSB0  /dev/ttyUSB1
```


정상적으로 인식된 것을 확인할 수 있었습니다. 


환경
---


```bash
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04 LTS
Release:	22.04
Codename:	jammy
```


결론
---


Ubuntu Linux 22.04에서 USB-to-Serial 장치를 연결했음에도 불구하고 
ttyUSB0와 같은 파일이 생성되지 않을 때는 
<code>/usr/lib/udev/rules.d/85-brltty.rules</code> 파일에서 
해당 부분을 주석 처리하고 재부팅하면 깔끔하게 해결이 됩니다. 







[✔️  Ubuntu Linux에서 ssmtp로 이메일 전송하는 초간단 방법 (이메일 전송 자동화)](001.html 'ssmtp 패키지를 이용하여 이메일을 전송하는 방법에 ')
---


ssmtp 패키지를 이용하여 이메일을 전송하는 방법에 대해서 설명합니다.


[✔️  공인 IP를 확인하는 방법(Windows, Ubuntu Linux 공통)](002.html 'Ubuntu Linux 쉘에서 공인 IP를 확인하는 방')
---


Ubuntu Linux 쉘에서 공인 IP를 확인하는 방법을 설명합니다. 


[✔️  Ubuntu Linux Crontab 실행 안됨 (crontab에서는 bash 문법 허용 안됨)](003-ubuntu-crontab-does-not-work.html '우분투 리눅스에서 crontabl이 실행되지 않는 문제 해결 방법에 ')
---


우분투 리눅스에서 crontabl이 실행되지 않는 문제 해결 방법에 대해서 설명합니다.


[✔️  모질라 썬더버드 메일 설정 방법 (네이버, gmail, 다음, 네이트)](004-thunderbird-email-setting-naver-gmail-daum.html 'Ubuntu Linux에서 기본적으로 제공하는 메일 프로그램인 모질라 썬더버드에 개인 메일 계정을 연결하는 방법에 ')
---


Ubuntu Linux에서 기본적으로 제공하는 메일 프로그램인 모질라 썬더버드에 개인 메일 계정을 연결하는 방법에 대해서 설명합니다.


[✔️  dead.letter 파일의 정체 (삭제 요망)](005-what-is-dead_letteres.html 'Ubuntu Linux 파일 시스템에 생성되는 dead.letter 파일의 정체를 알아보고 어떻게 다뤄야 하는지에 대해')
---


Ubuntu Linux 파일 시스템에 생성되는 dead.letter 파일의 정체를 알아보고 어떻게 다뤄야 하는지에 대해서 알아보겠습니다.


[✔️  우분투 리눅스에 서비스 등록하는 방법](006-ubuntu-register-serivce.html '우분투 리눅스에 python 스크립트를 서비')
---


우분투 리눅스에 python 스크립트를 서비스로 등록하는 방법


[✔️  vim 띄워쓰기 설정 방법](007-how-to-vim-setting.html 'vim 패키지의 ')
---


vim 패키지의 띄워쓰기 설정 방법


[✔️  우분투 리눅스에서 NetworkManager로 IP 설정 방법](009-ubuntu-network-manager-ip-setting.html '우분투 리눅스에서 IP를 설정하는 방법은 3가지가 있습니다. 그 중에서도 NetworkManager로 IP를 설정하는 방법에 ')
---


우분투 리눅스에서 IP를 설정하는 방법은 3가지가 있습니다. 그 중에서도 NetworkManager로 IP를 설정하는 방법에 대해서 설명합니다.


[✔️  색상 프로필을 만들려면 인증이 필요합니다.](010-ubuntu-xrdp-color-pkla.html 'XRDP 연결시 (색상 프로필을 만들려면 인증이 필요합니다.)라는 메시지가 반복적으로 표시')
---


XRDP 연결시 (색상 프로필을 만들려면 인증이 필요합니다.)라는 메시지가 반복적으로 표시될 경우 해결 방법


[✔️  Ubuntu Linux](index.html 'Ubuntu Linux에 대한 ')
---


Ubuntu Linux에 대한 내용을 기록합니다.
