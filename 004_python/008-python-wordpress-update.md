---
title: 파이썬으로 워드프레스 글 자동 발행하기
description: 파이썬으로 워드프레스 글을 자동 발행하는 방법에 대해서 설명합니다.
---


파이썬으로 워드프레스 글 자동 발행하기
===


파이썬으로 워드프레스 글을 자동 발행하는 방법에 대해서 설명합니다. 


### 패키지 설치


파이썬으로 워드프레스 글을 자동으로 발행하기 위해서는 
몇가지 패키지가 설치되어 있어야 합니다. 


- python-wordpress-xmlrpc 패키지
- php-xml 패키지


#### python-wordpress-xmlrpc 패키지 설치


아래의 명령으로 <code>python-wordpress-xmlrpc</code> 패키지를 설치합니다. 


```bash
$ sudo pip3 install python-wordpress-xmlrpc
```


만약 pip 패키지가 설치되어 있지 않다면 아래와 같은 에러가 뜹니다.


```
명령어 'pip' 을(를) 찾을 수 없습니다. 그러나 다음을 통해서 설치할 수 있습니다:

sudo apt install python3-pip
```


만약 pip 패키지가 설치되어 있지 않다면 
아래의 명령으로 <code>python3-pip</code> 패키지를 설치할 수 있습니다. 


```bash
$ sudo apt-get install python3-pip
```


#### pip-xml 패키지 설치


아래의 명령으로 <code>php-xml</code> 패키지를 설치합니다. 
만약 <code>php-xml</code> 패키지가 설치되어 있지 않으면 에러가 뜹니다. 


```bash
$ sudo apt-get install php-xml
```


php-xml 패키지를 설치했다면 아파치 웹서비스를 재시작 해줘야 합니다. 


```bash
$ sudo service apache2 restart
```


#### 파이썬 스크립트 작성


아래와 같이 파이썬 스크립트를 구성하고 실행하면 됩니다. 


```python
#!/usr/bin/python3

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts

def write_post(url, id, pw, title, slug, content):
  print("id :", id)
  print("pw :", pw)
  url = url + "/xmlrpc.php"
  print("url :", url)
  client = Client(url, id, pw)
  post = WordPressPost()
  post.title = title
  post.slug = slug
  post.content = content
  post.terms_names = {
                  'post_tag': 'wordpress',
                  'category' : ['']
  }

  post.post_status = 'publish'
  client.call(posts.NewPost(post))

if __name__ == '__main__':
  write_post( URL,
                  id,
                  pw,
                  "자동 글쓰기",
                  "자동 글쓰기 테스트",
                  "자동 글쓰기 본문")
```




[✔️  OpenCV를 이용하여 이미지를 출력하는 방법과 캠을 동작시키는 방법](001.html 'OpenCV를 이용해서 이미지를 출력하는 방법과 실시간으로 캠 영상을 표시하는 방법에 대해')
---


OpenCV를 이용해서 이미지를 출력하는 방법과 실시간으로 캠 영상을 표시하는 방법에 대해서 설명합니다.  


[✔️  파이선 터틀 그래픽을 이용해서 간단한 랜덤 문자 출력 방법](002.html '파이선 터틀 그래픽을 이용하여 간단한 랜덤 문자를 출력하는 방법에 ')
---


파이선 터틀 그래픽을 이용하여 간단한 랜덤 문자를 출력하는 방법에 대해서 설명합니다.


[✔️  파이썬 터틀 그래픽 재미있는 모양 예제](003-python-turtle-graphic-example.html '파이썬 터틀 그래픽을 이용해서 원, 삼각형, 사각형, 입체 모양의 별, 꽃, 바퀴 등의 재미있는 모양을 그려보는 ')
---


파이썬 터틀 그래픽을 이용해서 원, 삼각형, 사각형, 입체 모양의 별, 꽃, 바퀴 등의 재미있는 모양을 그려보는 예제를 제공합니다.


[✔️  파이썬 명령행 인자 사용 방법](003-python-명령행인자.html '파이썬 스크립트 실행시에 명령행 인')
---


파이썬 스크립트 실행시에 명령행 인자를 추가하는 방법


[✔️  파이썬 vim 띄워쓰기 설정 방법](004-python-vim-setting.html 'vim을 이용하여 파이썬 스크립트 편집시에 ')
---


vim을 이용하여 파이썬 스크립트 편집시에 띄워쓰기 설정 방법


[✔️  파이썬 홈디렉토리 파일 오픈 방법](005-python-cannot-read-home-directory.html '파이썬에서 홈 디렉토리의 파일을 오픈하는 방법에 ')
---


파이썬에서 홈 디렉토리의 파일을 오픈하는 방법에 대해서 설명합니다.


[✔️  파이썬 스크립트 실행시 No module named speech_recognition 에러가 발생했을 때 조치 방법](006-python-no-module-speech-recognition.html '파이썬 스크립트 실행시 No module named speech_recognition 이라는 에러가 발생했을 때 설치해야 하는 패키지명에 대')
---


파이썬 스크립트 실행시 No module named speech_recognition 이라는 에러가 발생했을 때 설치해야 하는 패키지명에 대해서 설명합니다. 


[✔️  파이썬에서 MP3 파일 비동기 재생 방법 (playsound async)](007-python-playsound.html '파이썬에서 MP3 파일 재생 방법과 playsound를 통해 비동기 재생 방식에 ')
---


파이썬에서 MP3 파일 재생 방법과 playsound를 통해 비동기 재생 방식에 대해서 설명합니다.


[✔️  Python](index.html 'Python 언어에 대한 내용을 기록')
---


Python 언어에 대한 내용을 기록하는 페이지입니다.


[🔽 다음글 : 파이썬 빈 배열 선언 방법](009-python-how-to-declare-empty-array.html '파이썬에서 빈 배열을 선언하는 방법에 ')
---


파이썬에서 빈 배열을 선언하는 방법에 대해서 설명합니다.


[✏️ ](https://www.github.com/boyinblue/boyinblue.github.io/edit/main/004_python/008-python-wordpress-update.md '수정하기')

