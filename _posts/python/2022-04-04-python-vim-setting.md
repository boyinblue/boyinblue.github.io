---
title: 파이썬 vim 띄워쓰기 설정 방법
permalink: /004_python/004-python-vim-setting.html
description: vim을 이용하여 파이썬 스크립트 편집시에 띄워쓰기 설정 방법
category: python
image: /assets/images/python/logo.png
---
파이썬은 띄워쓰기에 아주 민감한 프로그래밍 언어이다. 
이 페이지에서는 vim을 이용하여 파이썬 스크립트를 작성할 때 
띄워쓰기 오류를 줄이기 위한 설정 방법을 제공한다. 


C언어나 Java 언어에서의 중괄호
---


파이썬의 띄워쓰기 설정에 대해서 이야기하기에 앞서서 
왜 유독 파이썬에서만 띄워쓰기가 민감한지에 대해서 설정하겠다. 


기존의 C나 Java에서는 <code>{</code>와 </code>}</code>와 같은 
중괄호를 이용해서 for 구문 혹은 if 구문 등의 시작과 끝을 정의했다. 


```C
if( a == 10 )
{
    b = a;
}
```


위는 C언어에서 사용하는 중괄호의 예이다. 
if문의 시작과 끝을 알려주는 중괄호가 2개의 라인에 들어가기 때문에 
프로그래머 입장에서는 중괄호 입력이 제법 성가실 수 있다. 


또한 중괄호가 너무 많아서 코드가 컴팩트해보이지 못하기 때문에 
아래와 같이 중괄호를 입력하도록 코딩 규칙을 만들어 놓은 
프로젝트도 존재한다. 


```C
if( a == 10 ) {
    b = 1;
}
```


위와 같이 코드 블록의 시작을 알리는 <code>{</code>를 
if 구문의 끝에 위치시키면서 코드를 좀 더 간결하게 만들 수도 있다. 


위의 2가지 코딩 스타일은 프로그래머마다 호불호가 갈리기 때문에 
서로 다른 스타일로 코딩하는 프로그래머가 하나의 과제를 진행하다보면 
하나의 프로젝트에 여러 스타일의 코딩이 섞이게 된다. 


파이썬에서의 띄워쓰기는 문법의 일부이다.
---


하지만 파이썬은 띄워쓰기(indent)를 통해서 코드 블록의 
시작과 끝을 알려주는 방식이다. 


프로그래머는 기존의 <code>{</code>와 <code>}</code> 따위의 
중괄호를 입력하지 않아도 되기 때문에 가독성도 괜찮고 
시원시원하게 코드를 작성해 나갈 수 있는 장점이 있다. 


반면, 스페이스와 텝을 혼용할 경우 띄워쓰기 오류에 의해서 
원하지 않은 결과를 얻을 수도 있고, 
실행시에 수많은 띄워쓰기 에러 메시지를 만날 수 있다. 


vim 패키지 설치
---


처음 Ubuntu Linux를 설치하면 vi 명령이 제법 불편하다. 
키보드의 방향키가 제대로 동작하지 않는다. 
기본적인 vi의 경우 방향키 대신에 'h', 'j', 'k', 'l' 등의 키로
커서를 이동시키도록 되어 있기 때문이다.


vi 방향키


- 'h' : 왼쪽으로 이동
- 'j' : 아래로 이동
- 'k' : 위로 이동
- 'l' : 오른쪽으로 이동


일단 방향키부터 무척 불편하기 때문에 vim 패키지를 설치한다.


<code>$ sudo apt-get install vim</code>


vim 패키지를 설치한 이후에 <code>vi</code> 편집기를 열면 
키보드의 방향키가 정상적으로 잘 인식되는 것을 알 수 있다. 


파이썬 코딩을 위한 vim 설정
---


파이썬 코딩을 위한 vim 설정의 핵심은 
<code>Tab</code>을 <code>Space</code>로 바꿔주는 것에 있다. 


vim 설정 파일의 경로는 <code>~/.vimrc</code>다. 
선호하는 편집기로 <code>~/.vimrc</code> 파일을 편집해준다. 


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


[python.vim](/test/python/python.vim)


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
