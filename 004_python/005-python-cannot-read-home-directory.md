---
title: 파이썬 홈디렉토리 파일 오픈 방법
description: 파이썬에서 홈 디렉토리의 파일을 오픈하는 방법에 대해서 설명합니다.
---


파이썬 홈디렉토리 파일 오픈 방법
===


파이썬에서 홈 디렉토리의 파일을 오픈하는 방법에 대해서 설명합니다.


파이썬의 플랫폼 독립성과 홈 디렉토리
---


파이썬에서 홈 디렉토리 파일을 오픈하는 방법에 설명하기에 앞서서 
파이썬의 플랫폼 독립성에 대해서 잠깐 언급하고자 합니다. 


#### 파이썬의 플랫폼 독립성


파이썬이 프로그래밍 언어로써 널리 사랑을 받는 이유는 
여러가지가 있겠습니다만, 
그 중에서도 플랫폼에 dependent 하다는 것이 큰 장점이라고 생각합니다. 


만약 우리가 C언어로 어떤 프로그램을 제작한다면, 
윈도우즈용 프로그램과 리눅스용 프로그램을 2중으로 제작해야 합니다. 


간단한 콘솔 프로그램일 경우는 소스 코드는 공통이겠지만, 
윈도우즈에서도 컴파일을 해야 하고, 리눅스에서도 컴파일을 해야 합니다. 


반면, 파이썬 스크립트는 플랫폼(OS)에 독립적이기 때문에 
하나의 스크립트가 윈도우즈에서도 실행되고, 
리눅스에서도 잘 실행됩니다. 


필자가 Bash Shell Script를 몹시 아끼면서도 
파이썬에 관심을 갖게 된 배경에도 플랫폼에 종속적이지 않은 
파이썬의 특징 때문이었습니다. 


물론 윈도우즈에서 Bash Shell Script를 실행시킬 수 있는 
방법이 전혀 없는 것은 아니지만, 
리눅스에서의 쉘 스크립트 실행과 호환성이 상당히 떨어져서 
결국은 가급적이면 파이썬으로 스크립트를 작성하고 있습니다. 


#### 정말 플랫폼에 독립적인 것인가?


우리가 파이썬 패키지를 import 시켜서 사용할 때, 
윈도우즈와 리눅스를 가리지 않고 import 시켜서 사용하기 때문에 
파이썬이 플랫폼에 독립적인 것처럼 보일 수도 있겠습니다만, 
겉보기와는 달리 실상은 그렇지 않습니다. 


아래는 mp3 파일을 재생할 수 있는 <code>playsound</code>라는 패키지의 
스크립트 일부를 발췌한 것입니다. 


[출처 : https://github.com/TaylorSMarks/playsound](https://raw.githubusercontent.com/TaylorSMarks/playsound/master/playsound.py)


```python
from platform import system
system = system()

if system == 'Windows':
    playsound = _playsoundWin
elif system == 'Darwin':
    playsound = _playsoundOSX
    # 중략
else:
    playsound = _playsoundNix
    # 중략
```


외부에서는 <code>playsound</code>라는 함수를 플랫폼과 무관하게 사용하지만, 
내부는 OS에 따라서 구현이 다르다는 것을 알 수 있습니다. 


#### 리눅스의 홈 디렉토리 파일을 열 수 있는가?


그렇다면, 리눅스에서 널리 사용되는 홈 디렉토리에 있는 파일을 
파이썬에서 엑세스 할 수 있는가에 대해서 살펴보겠습니다. 


```python
def openFile(filename):
    fp = open("~/{}".format(filename))
    line = fp.readline()
    print(line)

openFile(".git-credentials")
```


위의 파이썬 스크립트는 홈 디렉토리의 <code>.git-credential</code> 파일을 
열어서 한 줄을 출력합니다. 


아주 간단한 스크립트이지만 실행해보면 아래와 같이 
<code>FileNotFoundError</code> 에러가 발생합니다. 


```python
$ python3 home_directory.py 
Traceback (most recent call last):
  File "home_directory.py", line 19, in <module>
    openFile(".git-credential")
  File "home_directory.py", line 4, in openFile
    fp = open("~/{}".format(filename))
FileNotFoundError: [Errno 2] No such file or directory: '~/.git-credentialis'
```


리눅스에서 홈 디렉토리를 의미하는 <code>~</code>를 
이해하지 못하기 때문입니다. 


#### 홈 디렉토리 파일을 여는 방법


아주 간단하게 홈 디렉토리 경로를 절대 경로로 넣어주면 
파일을 정상적으로 엑세스 할 수 있습니다. 


하지만 이런 내용을 언급하기 위해서 
이 글을 작성하고 있는것은 아닙니다. 


더군다나 사용자명에 따라서 절대 경로를 달라지기 때문에 
이 방법은 좋은 방법도 아닙니다. 


```python
def openFileByFullPath(full_path):
    fp = open(full_path)
    line = fp.readline()
    print(line)

openFileByFullPath("/home/boyinblue/.git-credential")
```


위와 같이 스크립트를 작성하고 실행을 하게 되면, 
원하는 결과를 얻기는 했지만, 뭔가 만족스럽지 못합니다. 


### expanduser 함수 사용


리눅스 홈디렉토리의 경로를 가져올 수 있는 
<code>expanderuser()</code> 함수를 사용하면 깔끔하게 해결됩니다. 


```python
def openFile2(filename):
    home_dir = os.path.expanduser('~')
    fp = open("{}/{}".format(home_dir, filename))
    line = fp.readline()
    print(line)

openFile2(".git-credentials")
```


<code>homd_dir = os.path.expanduser('~')</code> 구문에서 
우리가 원하던 <code>~</code>의 절대 경로를 가져올 수 있습니다. 


구문에서 미루어 짐작할 수 있듯이, <code>import os</code> 구문이 필요합니다. 


### 결론


리눅스의 홈 디렉토리인 <code>~</code> 경로 내부의 파일을 
파이썬에서 엑세스 하시려면 <code>os.path.expanduser('~')</code> 구문을 
사용하시면 되겠습니다. 







<!--001.html-->
[✔️  OpenCV를 이용하여 이미지를 출력하는 방법과 캠을 동작시키는 방법](001.html)
---


OpenCV를 이용해서 이미지를 출력하는 방법과 실시간으로 캠 영상을 표시하는 방법에 대해서 설명합니다.  


<!--002.html-->
[✔️  파이선 터틀 그래픽을 이용해서 간단한 랜덤 문자 출력 방법](002.html)
---


파이선 터틀 그래픽을 이용하여 간단한 랜덤 문자를 출력하는 방법에 대해서 설명합니다.


<!--003-python-turtle-graphic-example.html-->
[✔️  파이썬 터틀 그래픽 재미있는 모양 예제](003-python-turtle-graphic-example.html)
---


파이썬 터틀 그래픽을 이용해서 원, 삼각형, 사각형, 입체 모양의 별, 꽃, 바퀴 등의 재미있는 모양을 그려보는 예제를 제공합니다.


<!--003-python-명령행인자.html-->
[✔️  파이썬 명령행 인자 사용 방법](003-python-명령행인자.html)
---


파이썬 스크립트 실행시에 명령행 인자를 추가하는 방법


<!--004-python-vim-setting.html-->
[✔️  파이썬 vim 띄워쓰기 설정 방법](004-python-vim-setting.html)
---


vim을 이용하여 파이썬 스크립트 편집시에 띄워쓰기 설정 방법


<!--006-python-no-module-speech-recognition.html-->
[✔️  파이썬 스크립트 실행시 No module named speech_recognition 에러가 발생했을 때 조치 방법](006-python-no-module-speech-recognition.html)
---


파이썬 스크립트 실행시 No module named speech_recognition 이라는 에러가 발생했을 때 설치해야 하는 패키지명에 대해서 설명합니다. 


<!--007-python-playsound.html-->
[✔️  파이썬에서 MP3 파일 비동기 재생 방법 (playsound async)](007-python-playsound.html)
---


파이썬에서 MP3 파일 재생 방법과 playsound를 통해 비동기 재생 방식에 대해서 설명합니다.


<!--008-python-wordpress-update.html-->
[✔️  파이썬으로 워드프레스 글 자동 발행하기](008-python-wordpress-update.html)
---


파이썬으로 워드프레스 글을 자동 발행하는 방법에 대해서 설명합니다.


<!--_README.html-->
[✔️  Python](_README.html)
---


Python 언어에 대한 내용을 기록하는 페이지입니다.


<!--index.html-->
[✔️  Python](index.html)
---


Python 언어에 대한 내용을 기록하는 페이지입니다.


<!--001.html-->
[✔️  OpenCV를 이용하여 이미지를 출력하는 방법과 캠을 동작시키는 방법](001.html)
---


OpenCV를 이용해서 이미지를 출력하는 방법과 실시간으로 캠 영상을 표시하는 방법에 대해서 설명합니다.  


<!--002.html-->
[✔️  파이선 터틀 그래픽을 이용해서 간단한 랜덤 문자 출력 방법](002.html)
---


파이선 터틀 그래픽을 이용하여 간단한 랜덤 문자를 출력하는 방법에 대해서 설명합니다.


<!--003-python-turtle-graphic-example.html-->
[✔️  파이썬 터틀 그래픽 재미있는 모양 예제](003-python-turtle-graphic-example.html)
---


파이썬 터틀 그래픽을 이용해서 원, 삼각형, 사각형, 입체 모양의 별, 꽃, 바퀴 등의 재미있는 모양을 그려보는 예제를 제공합니다.


<!--003-python-명령행인자.html-->
[✔️  파이썬 명령행 인자 사용 방법](003-python-명령행인자.html)
---


파이썬 스크립트 실행시에 명령행 인자를 추가하는 방법


<!--004-python-vim-setting.html-->
[✔️  파이썬 vim 띄워쓰기 설정 방법](004-python-vim-setting.html)
---


vim을 이용하여 파이썬 스크립트 편집시에 띄워쓰기 설정 방법


<!--006-python-no-module-speech-recognition.html-->
[✔️  파이썬 스크립트 실행시 No module named speech_recognition 에러가 발생했을 때 조치 방법](006-python-no-module-speech-recognition.html)
---


파이썬 스크립트 실행시 No module named speech_recognition 이라는 에러가 발생했을 때 설치해야 하는 패키지명에 대해서 설명합니다. 


<!--007-python-playsound.html-->
[✔️  파이썬에서 MP3 파일 비동기 재생 방법 (playsound async)](007-python-playsound.html)
---


파이썬에서 MP3 파일 재생 방법과 playsound를 통해 비동기 재생 방식에 대해서 설명합니다.


<!--008-python-wordpress-update.html-->
[✔️  파이썬으로 워드프레스 글 자동 발행하기](008-python-wordpress-update.html)
---


파이썬으로 워드프레스 글을 자동 발행하는 방법에 대해서 설명합니다.


<!--_README.html-->
[✔️  Python](_README.html)
---


Python 언어에 대한 내용을 기록하는 페이지입니다.


<!--index.html-->
[✔️  Python](index.html)
---


Python 언어에 대한 내용을 기록하는 페이지입니다.


<!--001.html-->
[✔️  OpenCV를 이용하여 이미지를 출력하는 방법과 캠을 동작시키는 방법](001.html)
---


OpenCV를 이용해서 이미지를 출력하는 방법과 실시간으로 캠 영상을 표시하는 방법에 대해서 설명합니다.  


<!--002.html-->
[✔️  파이선 터틀 그래픽을 이용해서 간단한 랜덤 문자 출력 방법](002.html)
---


파이선 터틀 그래픽을 이용하여 간단한 랜덤 문자를 출력하는 방법에 대해서 설명합니다.


<!--003-python-turtle-graphic-example.html-->
[✔️  파이썬 터틀 그래픽 재미있는 모양 예제](003-python-turtle-graphic-example.html)
---


파이썬 터틀 그래픽을 이용해서 원, 삼각형, 사각형, 입체 모양의 별, 꽃, 바퀴 등의 재미있는 모양을 그려보는 예제를 제공합니다.


<!--003-python-명령행인자.html-->
[✔️  파이썬 명령행 인자 사용 방법](003-python-명령행인자.html)
---


파이썬 스크립트 실행시에 명령행 인자를 추가하는 방법


<!--004-python-vim-setting.html-->
[✔️  파이썬 vim 띄워쓰기 설정 방법](004-python-vim-setting.html)
---


vim을 이용하여 파이썬 스크립트 편집시에 띄워쓰기 설정 방법


<!--006-python-no-module-speech-recognition.html-->
[✔️  파이썬 스크립트 실행시 No module named speech_recognition 에러가 발생했을 때 조치 방법](006-python-no-module-speech-recognition.html)
---


파이썬 스크립트 실행시 No module named speech_recognition 이라는 에러가 발생했을 때 설치해야 하는 패키지명에 대해서 설명합니다. 


<!--007-python-playsound.html-->
[✔️  파이썬에서 MP3 파일 비동기 재생 방법 (playsound async)](007-python-playsound.html)
---


파이썬에서 MP3 파일 재생 방법과 playsound를 통해 비동기 재생 방식에 대해서 설명합니다.


<!--008-python-wordpress-update.html-->
[✔️  파이썬으로 워드프레스 글 자동 발행하기](008-python-wordpress-update.html)
---


파이썬으로 워드프레스 글을 자동 발행하는 방법에 대해서 설명합니다.


<!--_README.html-->
[✔️  Python](_README.html)
---


Python 언어에 대한 내용을 기록하는 페이지입니다.


<!--index.html-->
[✔️  Python](index.html)
---


Python 언어에 대한 내용을 기록하는 페이지입니다.
