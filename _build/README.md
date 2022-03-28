---
title: Script files to manage to this repository.
description: 본 디렉토리의 스크립트들은 본 레포지토리를 효율적으로 관리하기 위한 자동화 툴들입니다.
---


Scripts files to manage this repository
===


본 디렉토리의 스크립트들은 본 레포지토리를 효율적으로 관리하기 위한 자동화 툴들입니다. 


auto.sh
---


Crontab에 의해서 자동으로 실행되는 스크립트입니다. 
내부적으로 아래 3개의 스크립트를 순차적으로 실행합니다.


- auto.sh
  - [make\_site\_map.sh](#make\_site\_mapsh)
  - [make\_readme.sh](#make\_readmesh)
  - [send\_email.sh](#send\_emailsh)


<code>make\_site\_map.sh</code> 파일은 사이트맵을 생성하고 업데이트합니다. 


<code>make\_readme.sh</code> 파일은 사이트맵 파일을 기반으로 README.md 파일을 생성합니다.


<code>send\_email.sh</code> 파일은 사이트맵 및 README.md 파일의 변경점을 메일로 전송하는 스크립틥니다.


make\_site\_map.sh
---


### 목적


사이트맵 파일을 자동으로 생성하고 업데이트합니다. 


### 산출물


- sitemap.xml
- sitemap.txt


### xml 파일은 아래 형식으로 출력됩니다.


```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
<url>
  <loc>https://boyinblue.github.io/index.html</loc>
</url>
</urlset>
```


### 동작 과정


1. 루트 디렉토리에서 3자리 숫자로 시작하는 디렉토리들을 골라냅니다. 
2. 1에서 선택된 디렉토리들에서 확장자가 md인 파일들을 골라냅니다.
3. md 파일의 확장자를 html로 변환하여 사이트맵에 추가합니다.


make\_readme.sh
---


### 목적


사이트맵에 있는 파일들을 통해서 README.md 파일을 생성해냅니다. 


### 산출물


index.html 파일로 변환될 <code>README.md</code> 파일이 생성됩니다.
동시에 email로 변경점을 전송하기 위한 <code>tmp/diff.txt</code> 파일도 생성됩니다.


- README.md
- tmp/diff.txt


send\_email.sh
---


### 목적


make\_readme.sh 파일에서 생성된 변경점 파일을 e-mail로 전송합니다.
이 과정에서 <code>email\_header.txt</code> 파일과 
<code>tmp/diff.txt</code> 파일이 필요합니다. 


### 입력 파일


- email\_header.txt
- tmp/diff.txt


check\_md\_files.sh
---


### 목적


본 레포지토리에 존재하는 모든 md 파일들을 체크합니다. 
md 파일이 YAML 헤더를 가지고 있는지를 검사합니다. 


모든 MD 파일은 아래와 같은 형식의 YAML 헤더를 가지고 있어야 합니다.


```yaml
---
title: 본 페이지의 내용을 잘 대표하는 제목
description: 본 페이지에 대한 간략한 설명을 제공
---
```


check\_md\_files.py
---


### 목적


\check\_md\_files.sh 파일의 동작을 파이썬 스크립트로 작성하였습니다. 
추후 \check\_md\_files.sh 파일을 이 스크립트가 대체하도록 합니다.



