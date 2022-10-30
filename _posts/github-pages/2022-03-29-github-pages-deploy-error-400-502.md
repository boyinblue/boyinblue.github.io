---
title: GitHub Pages deploy 시에 400 에러나 502 에러가 발생할 경우 조치 방법
permalink: /002_github_blog/013-github-pages-deploy-error-400-502.html
description: GitHub Pages로 새로운 변경점을 반영하려고 할 때 400 에러나 502 에러가 발생할 경우 조치하는 방법입니다.
category: github-pages
---
어젯밤에 갑자기 GitHub Pages로 업데이트하는 모든 commit에 대해서 deploy가 되지 않는 문제가 발생했습니다. 


아시다시피, GitHub Pages는 레포지토리에 파일을 업로드하거나 수정하면, 
자동으로 build 및 deploy 과정이 진행됩니다. 


여러가지 시도들을 해봤었고, GitHub Pages 서비스 자체의 문제인 것으로 추정됩니다.


문제의 현상
---


개발자는 크든 작든 수많은 문제점들을 만나게 됩니다. 
가장 먼저 해야할 것들은 문제의 현상을 잘 살펴보고, 
여러가지 시도들을 하면서 결국에는 문제를 해결하게 됩니다. 


![Github Pages Deploy Error](/assets/images/013-github-pages-deploy-error-400-502.png)


제가 목격한 문제의 현상은 아래와 같습니다. 


1. GitHub Pages로 업데이트하는 모든 commit에 대한 deploy 작업이 실패함.
2. 기존에는 빌드와 디플로이를 합친 시간이 1분 내외로 소요되었으나, 문제의 상황에서는 10분에서 30분까지 소요되다가 결국에는 실패함.
3. 아래와 같은 실패 에러들을 deploy 로그에서 볼 수 있음.
   - Error: Timeout reached, aborting!
   - Error: Request failed with status code 502
   - Error: Request failed with status code 400
4. 마지막에 deploy된 웹페이지는 제대로 서비스되고 있음.


시도해본 것들
---


문제를 해결하거나 원인이 될 만한 것들을 살펴보기 위해서 시도한 것들입니다. 


가장 먼저, 제가 업로드한 변경점이 deploy 에러를 유발했을 수 있기 때문에, 
기존에 잘 deploy 되던 버전으로 revert 시켜서 확인해 보기도 했고, 
다른 계정으로 생성한 GitHub Pages를 deploy 시켜보기도 했습니다. 


아래의 3가지 시도 모두 실패했습니다. 


1. GitHub Pages에 업데이트한 변경점을 원복(revert) 시켜봄
   - 예전에 build 및 deploy에 문제 없던 버전에서도 deploy 에러가 발생함.
2. main branch가 아닌 별도의 branch를 생성해서 GitHub Pages를 연결해 봄
   - 여전히 deploy 에러가 발생함.
3. 다른 계정의 GitHub Pagee를 deploy 시켜봄.
   - 다른 계정의 GitHub Pages에서도 deploy 에러가 발생함.


의외의 해결 방법
---


이 문제는 GitHub Pages 서비스 자체에 문제가 있다고 생각하고, 
잊어버리고 기다리기로 했습니다. 


마지막으로 업로드한 페이지는 정상적으로 서비스되고 있기 때문에, 
추가로 제가 작업한 내용들이 긴급하게 웹서버에 deploy 될 필요는 없었기 때문입니다. 


아무리 GitHub Pages 서비스가 무료라고 하더라도, 
여러 계정에서 deploy 에러가 발생한다면 
GitHub Pgaes 서비스를 제공하는 측에는 상당히 부담스러운 문제이기 때문입니다. 


어젯밤에 발생한 문제를 깔끔하게 잊어버리고 잠을 청했습니다. 
오늘 아침 일찍 일어나서 다시 deploy 시켜봤더니 정상적으로 수행됩니다. 


결론
---


GitHub Pages deploy에러가 발생했다면 변경점이 deploy 에러를 유발한 것은 아닌지 살펴봅니다. 


만약, 이전에 잘 deploy 되던 버전으로 revert 했음에도 불구하고 
지속적인 에러가 발생한다면 GitHub Pages 자체의 문제일 수 있으므로 
복구 될 때까지 기다려보시기 바랍니다. 


참고할 만한 페이지
---


만약 deploy 에러가 아니라 build 에러라면 아래의 페이지를 참조하세요. 


[GitHub Pages 빌드 에러 조치 방법](010-github-no-uploaded-artifact-was-found.html)


이상입니다. 
