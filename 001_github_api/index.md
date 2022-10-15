---
title: GitHub API
description: GitHub API 사용 방법 및 관련 팁을 제공합니다.
---


GitHub API
===


많은 SW 개발자들이 깃헙(GitHub)을 사용하고 있습니다. 
GitHub는 훌륭한 형상관리 시스템임에 틀림없습니다. 


필자의 경우는 CC(Clear Case)와 Perforce와 Git을 모두 사용해봤는데, 
그 중에서 Git이 가장 편리하고 효율적으로 형상 관리가 가능했습니다. 


특히 상당히 RESTful한 <code>GitHub API</code>는 아주 잘 디자인되어 있고, 
개발자의 시간과 노력을 현저하게 절약해줍니다. 


많은 개발자들이 <code>git 명령</code> 또는 GUI 프로그램 등을 이용해서 
프로젝트 협업을 하는데 익숙해져 있다고 생각합니다. 


하지만 <code>GitHub API</code>를 이용하면 훨씬 더 많은 것들을 수행할 수 있습니다. 
특히, Jenkins와 GitHub를 연동하면 상당히 많은 것들을 자동화할 수 있습니다. 


예를들면, GitHub에 PR(Pull Request)가 생성되면 해당 정보가 Jenkins로 전달되고, 
Jenkins는 일련의 빌드 테스트 및 자동 테스트를 수행한 이후에 
해당 GitHub PR에 수행 결과를 알려줍니다. 


이 과정에 GitHub API를 응용하며 아래와 같은 작업들을 자동화할 수 있습니다.
1. GitHub Pull Request에 코멘트(Comment)를 남길 수 있습니다.
2. GitHub Pull Request에 레이블(Label)을 달거나 제거할 수 있습니다.


이 외에도 응용할 수 있는 방법은 무궁무진합니다. 


본 페이지에서는 GitHub API 관련된 내용들을 다룹니다. 
1. GitHub API 호출 방법 (curl 명령, hub 프로그램)
2. GitHub API 팁
3. GitHub API 문제 발생시 트러블 슈팅 방법





[✔️ GitHub API 호출시 Bad Credentials 에러 발생시 조치 방법](001_bad_credential.html '본 페이지에서는 GitHub API 호출시에 Bad credentials 응답이 오는 문제를 해결하는 방법을 기술하고자 합니다.')
---


본 페이지에서는 GitHub API 호출시에 Bad credentials 응답이 오는 문제를 해결하는 방법을 기술하고자 합니다.


[✔️ GitHub API .git-credentials 파일로부터 id와 token을 안전하게 파싱하는 방법](002_get_token_from_credential_file.html 'Bash 쉘 스크립트 및 파이썬 스크립트를 이용하여 GitHub 토큰를 파싱하는 방법을 설명합니다.')
---


Bash 쉘 스크립트 및 파이썬 스크립트를 이용하여 GitHub 토큰를 파싱하는 방법을 설명합니다.


[✔️ server certificate verification failed. CAfile none CRLfile none 에러 조치 방법](003-server-certificate-verification-fail.html 'GitHub 서버로부터 통신을 시도할 때 server certificate verification failed. CAfile none CRLfile none 에러가 발생할 경우 조치하는 방법에 대해서 설명합니다.')
---


GitHub 서버로부터 통신을 시도할 때 server certificate verification failed. CAfile none CRLfile none 에러가 발생할 경우 조치하는 방법에 대해서 설명합니다.


[✔️ GitHub에서 레포지토리의 생성일을 확인하는 방법](004-github-how-to-get-the-creation-date-of-repository.html 'GitHub API를 이용해서 레포지토리의 생성일을 확인하는 방법에 대해서 설명합니다.')
---


GitHub API를 이용해서 레포지토리의 생성일을 확인하는 방법에 대해서 설명합니다.


[✏️ ](https://www.github.com/boyinblue/boyinblue.github.io/edit/main/001_github_api/index.md '수정하기')

