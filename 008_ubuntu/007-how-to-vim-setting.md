---
title: vim 띄워쓰기 설정 방법
description: vim 패키지의 띄워쓰기 설정 방법
---


본 페이지에서는 vim 패키지 설치 방법과 띄워쓰기 설정 방법에 대해서 설명한다. 


vim 패키지 설치
===


Ubuntu Linux를 처음 설치하게 되면 기본적으로 vi 에디터를 사용 가능하다. 
리눅스를 오래동안 사용해온 필자에게도 vi 사용은 제법 불편하다.


특히, 키보드의 방향키가 제대로 동작하지 않는다. 
그 이유는 기본적인 vi의 경우 방향키 대신에 'h', 'j', 'k', 'l' 등의 키로
커서를 이동시키도록 되어 있기 때문이다.


vi 방향키


- 'h' : 왼쪽으로 이동
- 'j' : 아래로 이동
- 'k' : 위로 이동
- 'l' : 오른쪽으로 이동


vim 패키지를 설치하면 방향키를 사용할 수 있기 때문에 
꼭 vim 패키지를 설치하시기를 강력하게 추천한다. 


<code>$ sudo apt-get install vim</code>


vim 패키지를 설치한 이후에 <code>vi</code> 편집기를 열면 
키보드의 방향키가 정상적으로 잘 인식되는 것을 알 수 있다. 


코딩 컨벤션과 띄워쓰기
===


SW 개발자나 FW 개발자에게 띄워쓰기는 아주 중요하다. 
하나의 프로젝트를 여러 사람들이 동시에 협업을 하다보면, 
사람마다 코딩 스타일이 다르기 때문에 상당히 성가신 경우가 많다. 


예를 들면, C언어에서 중괄호를 어떻게 사용할 것인가부터 시작해서, 
텝(Tab)을 허용할 것인지, 텝을 허용한다면 공백을 몇개로 할 것인지 등 
개발자마다 선호하는 스타일이 다르기 때문에 
코딩 컨벤션이라는 것을 만들어서 비슷한 형식으로 코딩을 하도록 
유도하는 회사들도 있다. 


특히 파이썬 언어의 경우 공백 자체가 문법의 일부이고, 
이 부분을 상당히 민감하게 체크하기 때문에 
더욱 더 공백(indent)가 중요하다고 할 수 있다. 


파이썬 vim 띄워쓰기 설정 방법에 대해서 관심있다면, 
[파이썬 vim 띄워쓰기 설정 방법](https://boyinblue.github.io/004_python/004-python-vim-setting.html) 글을 참조하시기 바란다. 


vim 띄워쓰기 설정을 통해서 아래의 설정들이 가능하다.


- 텝을 허용할 것인가?
- 텝을 허용한다면 몇 글자를 띄울 것인가? 
- 텝을 공백으로 변환한다면 공백 몇개로 할 것인가? 


위와 같은 설정은 vim 실행 중에 명령을 통해서도 가능하고, 
설정 파일에 담게 되면 vim을 실행할때마다 자동으로 설정되도록 할 수도 있다. 
또한, 언어에 따라서 다르게 설정도 가능하다.


vim 설정파일 예시
---


선호하는 편집기로 <code>~/.vimrc</code> 파일을 편집한다. 


```bash
$ vi ~/.vimrc
```


```
syntax on
filetype indent plugin on
set tabstop=4
set expandtab!
set softtabstop=4
set nu

let g:python_recommended_style=0
```


위의 설정은 필자가 선호하는 vim 설정이다. 
그런데 다소 이해가 되지 않는 부분이 있을 것이다. 


파이썬에서는 <code>Tab</code>을 <code>Space</code>로 
변경해주는 것이 핵심이라고 하면서 
<code>set expandtab!</code> 설정을 통해서 
오히려 텝을 스페이스로 바꿔주지 않도록 하고 있다. 


필자는 기본적으로 C언어 작업과 파이썬을 병행한다. 
또한 C언어로 코딩할때 텝은 4칸을 선호한다. 


따라서 필자가 C언어로 코딩할때는 텝을 그대로 사용 가능하고, 
텝은 공백 4칸으로 설정이 된다. 


반면, 파이썬으로 코딩할때는 아래 구문에 의해서 
텝이 자동으로 스페이스로 변환된다.


<code>let g:python_recommended_style=0</code>


위의 코드 이전에 설정한 값들이 
<code>let g:python_recommended_style=0</code> 설정에 의해서 
overwrite될 수 있음을 유의한다. 


예를들면, <code>set expand tab!</code>과 같은 설정은 
python 스크립트 편집시에는 전혀 먹히지 않는다는 것이다. 


python syntax 파일 다운로드 방법
---


python syntax 파일은 아래 위치에서 다운로드 받을 수 있다. 


[https://www.vim.org/scripts/script.php?script_id=790](https://www.vim.org/scripts/script.php?script_id=790)


python.vim 파일은 <code>~/.vim/syntax</code> 경로에 저장하면 된다. 


위의 페이지에 접속하는게 번거롭다면 아래 링크에서 다운로드 받으면 된다.


[python.vim](python.vim)


아래의 명령으로 한 번에 다운로드가 가능하다.


```bash
$ mkdir -p ~/.vim/syntax
$ wget -O ~/.vim/syntax/syntax.vim https://boyinblue.github.io/004_python/python.vim
```


결론
---


파이썬은 띄워쓰기에 아주 민감한 언어이다. 
그 이유는 파이썬에서의 씌워쓰기는 문법의 일부이기 때문이다. 


vim에서 파이썬 스크립트를 편리하게 편집하기 위한 
설정 방법에 대해서도 언급하였다. 




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


[✔️  USB-to-Serial 장치를 연결했지만 /dev/tty/ttyUSB0 파일이 생성되지 않는 경우 조치 방법](008-usb-to-serial-no-ttyUSB0.html 'Ubuntu Linux 22.04에 USB-to-Serial 장치를 연결했지만 ttyUSB0 파일이 생성되지 않는 경우 조치하는 방법에 ')
---


Ubuntu Linux 22.04에 USB-to-Serial 장치를 연결했지만 ttyUSB0 파일이 생성되지 않는 경우 조치하는 방법에 대해서 설명합니다.


[✔️  우분투 리눅스에서 NetworkManager로 IP 설정 방법](009-ubuntu-network-manager-ip-setting.html '우분투 리눅스에서 IP를 설정하는 방법은 3가지가 있습니다. 그 중에서도 NetworkManager로 IP를 설정하는 방법에 ')
---


우분투 리눅스에서 IP를 설정하는 방법은 3가지가 있습니다. 그 중에서도 NetworkManager로 IP를 설정하는 방법에 대해서 설명합니다.


[✔️  색상 프로필을 만들려면 인증이 필요합니다.](010-ubuntu-xrdp-color-pkla.html 'XRDP 연결시 (색상 프로필을 만들려면 인증이 필요합니다.)라는 메시지가 반복적으로 표시')
---


XRDP 연결시 (색상 프로필을 만들려면 인증이 필요합니다.)라는 메시지가 반복적으로 표시될 경우 해결 방법


[✔️  Ubuntu Linux](index.html 'Ubuntu Linux에 대한 ')
---


Ubuntu Linux에 대한 내용을 기록합니다.
