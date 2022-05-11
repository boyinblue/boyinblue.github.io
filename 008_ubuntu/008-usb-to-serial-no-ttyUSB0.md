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


<code>
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04 LTS
Release:	22.04
Codename:	jammy
</code>


결론
---


Ubuntu Linux 22.04에서 USB-to-Serial 장치를 연결했음에도 불구하고 
ttyUSB0와 같은 파일이 생성되지 않을 때는 
<code>/usr/lib/udev/rules.d/85-brltty.rules</code> 파일에서 
해당 부분을 주석 처리하고 재부팅하면 깔끔하게 해결이 됩니다. 



