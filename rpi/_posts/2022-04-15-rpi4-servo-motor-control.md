---
title: 마이크로 서보 9G 모터 핀 번호 (라즈베리파이4B 서보 모터 제어 방법)
permalink: /010_raspberry/003-rpi4-servo-motor-control.html
description: 마이크로 서보 9G 모터 핀 번호 및 라즈베리파이4B에서 서보 모터 제어 방법 설명
categpry: rpi
---


마이크로 5V 서보 모터 핀 번호 (라즈베리파이4B 서보 모터 제어 방법)
===


본 페이지에서는 라즈베리파이 및 아두이노에서 교육용으로 널리 사용중인 
마이크로 서보 9G 모터에 대해서 설명합니다. 


#### 마이크로 9G 서보 모터란?


모터의 종류는 상당히 다양합니다. 
DC 모터, 스텝 모터, BLDC 모터, 서보 모터 등 다양한 모터들이 있습니다. 


오늘은 서보 모터 중에서도 라즈베리파이나 아두이노에서 
교육용으로 널리 사용중인 마이크로 9G 서보 모터에 대해서 설명드리겠습니다. 


마이크로 9G 서보 모터는 회전 반영이 0도 ~ 180도의 모터입니다. 
PWM 신호를 통해서 모터의 각도를 제어할 수 있습니다. 


하지만 저가의 교육용 서보 모터라서 원하는 각도로 정밀하게 제어가 불가하고, 
토크 또한 약해서 작은 부하에도 동작하지 못하는 단점이 있습니다. 


#### 서보 모터 핀번호


![서보 모터 핀번호](/assets/images/003-rpi4-servo-motor-control.jpg)


|핀 번호|색  깔|설  명|비  고|
|--|--|--|--|
|1|주황색|PWM|모터 제어를 위한 PWM 신호|
|2|빨간색|VCC|5V|
|3|갈색|GND|    |


위의 사진에 보이는 마이크로 서보 9G 모터는 5V로 동작합니다. 
이 때문에 2번 핀과 3번 핀에 5V를 인가합니다. 


1번 핀에 PWM을 이용하여 서보 모터의 각도를 제어할 수 있습니다. 


#### PWM 제어 가능한 핀번호


VCC와 GND는 라즈베리파이의 어디에 연결해야 하는지 
전혀 고민없이 연결하면 됩니다. 


반면, PWM 신호의 경우는 어느 핀에 연결해야 하는지 
살펴볼 필요가 있습니다. 


그 이유는 <code>Alt Function</code>으로 PWM을 지원하는 핀을 
선택해야 하기 때문입니다. 


정답지부터 말씀드리자면 PWM 제어가 가능한 핀 번호는 
<code>GPIO 12</code>, <code>GPIO 13</code>, 
<code>GPIO 18</code>, <code>GPIO 19</code> 총 4개입니다. 


자세한 핀맵은 아래 테이블을 참고하시기 바랍니다. 


|GPIO|Pull|ALT0|ALT1|ALT2|ALT3|ALT4|ALT5|
|--|--|--|--|--|--|--|--|
|0|High|SDA0|SA5|PCLK|SPI3 CE0 N|TXD2|SDA6|
|1|High|SCL0|SA4|DE|SPI3 MISO|RXD2|SCL6|
|2|High|SDA1|SA3|LCD VSYNC|SPI3 MOSI|CTS2|SDA3|
|3|High|SCL1|SA2|LCD HSYNC|SPI3 SCLK|RTS2|SCL3|
|4|High|GPCLK0|SA1|DPI D0|SPI4 CE0 N|TXD3|SDA3|
|5|High|GPCLK1|SA0|DPI D1|SPI4 MISO|RXD3|SCL3|
|6|High|GPCLK2|SOE N|DPI D2|SPI4 MOSI|CTS3|SDA4|
|7|High|SPI0 CE1 N|SWE N|DPI D3|SPI4 SCLK|RTS3|SCL4|
|8|High|SPI0 CE0 N|SD0|DPI D4|-|TXD4|SDA4|
|9|Low|SPI0 MISO|SD1|DPI D5|-|RXD4|SCL4|
|10|Low|SPI0 MOSI|SD2|DPI D6|-|CTS4|SDA5|
|11|Low|SPI0 SCLK|SD3|DPI D7|-|RTS4|SCL5|
|12|Low|PWM0|SD4|DPI D8|SPI5 CE0 N|TXD5|SDA5|
|13|Low|PWM1|SD5|DPI D9|SPI5 MISO|RXD5|SCL5|
|14|Low|TXD0|SD6|DPI D10|SPI5 MOSI|CTS5|TXD1|
|15|Low|RXD0|SD7|DPI D11|SPI5 SCLK|RTS5|RXD1|
|16|Low|FL0|SD8|DPI D12|CTS0|SPI1 CE2 N|CTS1|
|17|Low|FL1|SD9|DPI D13|RTS0|SPI1 CE1 N|RTS1|
|18|Low|PCM CLK|SD10|DPI D14|SPI6 CE0 N|SPI1 CE0 N|PWM0|
|19|Low|PCM FS|SD11|DPI D15|SPI6 MISO|SPI1 MISO|PWM1|
|20|Low|PCM DIN|SD12|DPI D16|SPI6 MOSI|SPI1 MOSI|GPCLK0|
|21|Low|PCM DOUT|SD13|DPI D17|SPI6 SCLK|SPI1 SCLK|GPCLK1|
|22|Low|SD0 CLK|SD14|DPI D18|SD1 CLK|ARM TRST|SDA6|
|23|Low|SD0 CMD|SD15|DPI D19|SD1 CMD|ARM RTCK|SCL6|
|24|Low|SD0 DAT0|SD16|DPI D20|SD1 DAT0|ARM TDO|SPI3 CE1 N|
|25|Low|SD0 DAT1|SD17|DPI D21|SD1 DAT1|ARM TCK|SPI4 CE1 N|
|26|Low|SD0 DAT2|TE0|DPI D22|SD1 DAT2|ARM TDI|SPI5 CE1 N|
|27|Low|SD0 DAT3|TE1|DPI D23|SD1 DAT3|ARM TMS|SPI6 CE1 N|


#### 서보 모터 제어 예제


아래는 파이썬을 이용한 서보 모터 제어 예제입니다. 


```python
#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

pin_num = None

def serbo_init(serbo_pin_num = 18):
    global pin_num

    GPIO.setmode(GPIO.BCM)
    pin_num = serbo_pin_num
    GPIO.setup(pin_num, GPIO.OUT)

def set_degree(degree):
    phz = GPIO.PWM(pin_num, 100)
    phz.start(5)
    duty = degree / 10.0 + 2.5
    phz.ChangeDutyCycle(duty)
    time.sleep(0.5)

def main():
    while True:
        degree = float( input("제어할 각도 :") )
        set_degree(degree)

    GPIO.cleanup()

if __name__ == '__main__':
    serbo_init()
    main()
```


#### 결론


라즈베리파이 및 아두이노에서 교육용으로 널리 사용중인 
마이크로 서보 9G 모터에 대한 간략한 설명 및 
제어 예제에 대한 설명을 모두 마칩니다. 







[✔️  '라즈베리파이로 GPIO 제어시 \"RuntimeError: Not running on a RPi!\" 문제 해결 방법 (3가지)'](001-not-running-on-RPi.html ''파이선으로 작성한 GPIO 제어 스크립트가 "RuntimeError: Not running on a RPi!"라는 메시지와 함께 수행되지 못하는 문제를 해결하는 방법에 대')
---


'파이선으로 작성한 GPIO 제어 스크립트가 "RuntimeError: Not running on a RPi!"라는 메시지와 함께 수행되지 못하는 문제를 해결하는 방법에 대해서 설명합니다.'


[✔️  라즈베리파이4B에서 리모컨 입력 받아서 처리하는 방법 (Ubuntu 21.10)](002-rpi4-ir-receiver-ubuntu-21-10.html '라즈베리파이4B에서 리모컨 입력 받아서 처리하는 방법 (Ubu')
---


라즈베리파이4B에서 리모컨 입력 받아서 처리하는 방법 (Ubuntu 21.10)


[✔️  Raspberry Pi](index.html '초소형 미니 컴퓨터인 라즈베리파이 관련 연구 ')
---


초소형 미니 컴퓨터인 라즈베리파이 관련 연구 내용을 정리합니다.


[✏️ ](https://www.github.com/boyinblue/boyinblue.github.io/edit/main/010_raspberry/003-rpi4-servo-motor-control.md '수정하기')

