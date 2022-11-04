---
title: 파이썬으로 워드프레스 글 자동 발행하기
permalink: /004_python/008-python-wordpress-update.html
description: 파이썬으로 워드프레스 글을 자동 발행하는 방법에 대해서 설명합니다.
category: python
image: /assets/images/python/logo.png
---
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
