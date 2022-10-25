---
title: Beyond Compare에서 화이트 스페이스 표시하는 방법
description: 공백은 스페이스나 텝으로 구성되어 있습니다. Beyond Compare에서 white space를 표시하는 방법을 설명합니다.
category: beyond-compare
image: /assets/images/beyond-compare/beyond-compare-whitespace.png
---

요약
---


Beyond Compare에서 화이트 스페이스(white space)를 표시하기 위해서는 
`View' - 'Visible Whitespace' 메뉴를 선택하면 된다.


White Space란?
---


White Space란 눈에는 그저 하얗게 보이는 공백 문자를 의미한다. 
<kbd> Space </kbd>나 <kbd> Tab </kbd>으로 구성된 부분이다. 


White Space의 중요성
---


SW 개발자에게 공백(white space)는 상당히 중요한 부분이다. 
공백이 스페이스(0x20)로 구성되어 있는지, 텝으로 구성되어 있는지가 
다르게 동작하는 경우가 있을 수 있기 때문이다. 


### C언어 인덴트 문제


C언어에서의 indent는 소스 코드의 가독성을 향상시키는데 도움이 된다. 
인덴트를 공백 4개로 사용할 것인지, 공백 8개로 사용할 것인지는 
프로그래머에게 아주 중요한 문제일 수 있다. 


A와 B가 공동의 프로젝트를 진행한다고 가정해보자. 
A의 개발 환경은 텝이 공백 4개에 해당하는 크기이고, 
B는 텝이 공백 8개에 해당하는 크기이다. 


A가 작업한 코드를 B가 열었을 때 텝이 공백 8개로 표기되는 문제가 발생한다. 
이 때문에 indent는 텝을 사용하지 말고 스페이스로만 구성하도록 하는 
code convention을 구성하는 팀도 있다. 


### 파이썬은 indent가 문법의 일부이다.


파이썬에서는 인덴트가 단순한 가독성을 높이기 위한 측면 뿐만 아니라, 
문법의 일부라고 할 수 있다. 
파이썬에서는 <kbd>{</kbd> 또는 <kdb>}</kbd> 같은 명시적인 부호 없이 
인덴트를 이용해서 코드 블록을 구분하기 때문이다. 


따라서, 파이썬에서 인덴트가 맞지 않을 경우 
indent 문법 오류를 발생시킬 수 있다. 


Beyond Compare에서 white space 설정
---


![Beyond Compare에서 white space 설정 방법](/assets/images/beyond-compare/beyond-compare-visible-whitespace.png 'Beyond Compare에서 white space 설정 방법')


Beyond Compare에서 화이트 스페이스(white space)를 
표기할 수 있는 기능을 제공한다. 


### 화이트 스페이스 설정 메뉴


>메뉴에서 `View`를 선택한 이후에, 'Visible Whitespace'를 선택하면 된다. 


### 단축키


<kbd> Alt </kbd> + <kbd> V </kbd> + <kbd> W </kbd>를 입력하면 
Whitespace 표시를 토글링할 수 있다. 
