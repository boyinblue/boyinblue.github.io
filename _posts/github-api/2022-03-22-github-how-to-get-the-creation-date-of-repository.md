---
title: GitHub에서 레포지토리의 생성일을 확인하는 방법
permalink: /001_github_api/004-github-how-to-get-the-creation-date-of-repository.html
description: GitHub API를 이용해서 레포지토리의 생성일을 확인하는 방법에 대해서 설명합니다.
category: github-api
---
GitHub Pages를 생성하고 16일만에 구글의 애드센스를 게시할 수 있게 되었습니다. 
웹 페이지를 처음 생성한 초기에는 사용법에 익숙하지 않아서 많이 힘들었습니다. 
아시다시피 GitHub Pages는 GitHub에서 관리되는 웹서버입니다. 
무료로 사용할 수 있는데다가 GitHub의 형상 관리 기능을 그대로 사용할 수 있기 때문에 컨텐츠 관리에도 효율적입니다.


나름 SW 개발을 약 15년 가까이 하고 있어서 GitHub에 상당히 익숙하니다만, 
GitHub Pages용 레포지토리를 언제 생성했는지 막상 확인하려 했더니 어떻게 확인해야 될지 조금 막막하더군요.   
API 호출을 통해서 깃헙 저장소의 생성일을 확인할 수 있는 방법에 대해서 설명드리겠습니다.


GitHub API를 이용해서 레포지토리의 생성일을 확인하는 방법 (웹브라우저 이용)
---


GitHub API를 이용하면 레포지토리의 생성일을 손쉽게 확인할 수 있습니다. 
난이도는 아주 낮기 때문에 누구든지 어렵지 않게 확인할 수 있습니다. 
웹브라우저에 아래와 같은 형식으로 입력해보면 됩니다. 


```html
https://api.github.com/repos/{username}/{repository name}
```


예를 들어서 username이 boyinblue이고, repo명이 boyinblue.github.io 라면 아래와 같이 입력하면 됩니다. 


```html
https://api.github.com/repos/boyinblue/boyinblue.github.io
```


실행 결과는 아래와 같습니다. 


![GitHub 레포지토리의 생성일을 확인하는 방법](/asset/images/github-api/004-github-how-to-get-creation-date-of-repository.png "GitHub 레포지토리의 생성일을 확인하는 방법")


GitHub API의 응답은 json 형식으로 리턴됩니다. 
그 중에서도 "created_at" 항목을 보시면 언제 생성되었는지 확인하실 수 있습니다. 


```json
  "releases_url": "https://api.github.com/repos/boyinblue/boyinblue.github.io/releases{/id}",
  "deployments_url": "https://api.github.com/repos/boyinblue/boyinblue.github.io/deployments",
  "created_at": "2022-03-06T06:20:09Z",
  "updated_at": "2022-03-21T15:23:44Z",
  "pushed_at": "2022-03-22T00:25:25Z",
  "git_url": "git://github.com/boyinblue/boyinblue.github.io.git",
  "ssh_url": "git@github.com:boyinblue/boyinblue.github.io.git",
  "clone_url": "https://github.com/boyinblue/boyinblue.github.io.git",
  "svn_url": "https://github.com/boyinblue/boyinblue.github.io",
```


제 GitHub Pages는 2022년 3월 6일에 생성되었다는 것을 확인할 수 있습니다.


GitHub API를 이용해서 레포지토리의 생성일을 확인하는 방법 (curl 명령 이용)
---


위와 같이 웹브라우저에서 확인하는 방법은 다소 불편함이 있습니다. 
사람이 손으로 웹브라우저에 주소를 입력해줘야하고, 그 결과도 찾아봐야되기 때문입니다. 
우선 웹브라우저 없이 curl 명령을 통해서 확인하는 방법에 대해서 설명드리겠습니다. 
웹 브라우저에 입력했던 URL을 curl 명령 인자로 넣어주기만 하면 됩니다.


```bash
$ curl https://api.github.com/repos/boyinblue/boyinblue.github.io
```


아까 웹브라우저로 살펴봤던 내용과 동일한 내용이 json으로 출력됩니다. 
다음 단계는, 출력되는 json 중에서 필요한 내용만 추출하는 것입니다. 
Ubuntu Linux 기준으로 <code>jq</code>라는 패키지를 사용하면 손쉽게 파싱할 수 있습니다. 


혹시 jq 패키지가 설치되어 있지 않다면 <code>$ sudo apt-get install jq</code> 명령을 통해서 설치해줍니다.
이미 jq 패키ㅣ가 설치되어 있다면 아래 과정은 생략하시면 됩니다. 


```bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install jq
```


설치가 완료되었는지 확인하기 위해서 <code>jq --version</code> 명령을 입력해줍니다.


```bash
$ jq --version
```


패키지가 제대로 설치되었다면 아래와 같이 jq 패키지의 버전이 표시되게 됩니다. 


```bash
jq-1.6
```


이제 본격적으로 jq를 이용해서 레포의 생성일을 확인할 차례입니다.


```bash
$ curl https://api.github.com/repos/boyinblue/boyinblue.github.io | jq '.created_at'
```


레포지토리의 생성일이 UTC(세계 협정시)를 기준으로 표기됩니다. 


```bash
"2022-03-06T06:20:09Z"
```


실행 결과를 살펴보면 json 데이터 중에서 created_at 이라는 항목만 표시된 것을 알 수 있습니다. 
crul 명령을 통해서 표준출력으로 튀어나오는 json 데이터를 다시 파이프를 통해서 jq에 공급해주는 명령입니다. 
jq는 json 데이터중에서 created_at 항목만 추출해서 출력해줍니다.


한가지 아쉬운 점은 결과값이 쌍따움표 안에 표기되어 있다는 것입니다. 
쌍다움표를 제거시키기 위해서 xargs 라는 명령을 사용하겠습니다. 


```bash
$ curl https://api.github.com/repos/boyinblue/boyinblue.github.io | jq '.created_at' | xargs
```


위와 같이 수행하면 쌍따움표가 제거된 상태로 레포지토리의 생성일이 출력됩니다. 


```bash
2022-03-06T06:20:09Z
```


xargs 명령을 거치면서 쌍따움표가 제거되어 원하는대로 깔끔하게 출력되었습니다.  


결론
---


본 페이지에서는 GitHub Repoitory의 생성일을 확인하는 방법에 대해서 살펴보았습니다.


이상입니다.   
