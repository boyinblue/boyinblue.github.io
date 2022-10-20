---
title: Jenkins Hook이 제대로 전달되지 못하는 경우 해결 방법 (GitHub Pull Request Builder 오류 및 역방향 프록시 설정 오류)
permalink: /003_jenkins/001.html
description: Jenkins에서 GitHub Pull Request Builder가 역방향 프록시 설정 오류 메시지가 발생하면서 빌드되지 않는 오류를 해결하는 방법에 대해서 설명합니다. 
---
GitHub와 Jenkins를 연동해두면, GitHub에 Pull Request가 등록되면 자동으로 Jenkins쪽에 Hook이 전달됩니다. 
GitHub Pull Request Builder가 제대로 트리거되지 못하는 문제가 발생했습니다. 
Jenkins의 GitHub Pull Request Builder가 제대로 시작되지 못하는 원인은 여러가지가 있겠습니다만, 
그 중에서도 특별히 Jenkins 서버의 주소 설정이 올바르지 않아서 "역방향 프록시 설정 오류" 에러가 뜨는 상태의 문제에 대해서 기술하고자 합니다.    

   
Jenkins의 GitHub Pull Request Builder란?
---

   
어쩌면 TMI일 수도 있겠지만, Jenkins에서는 GitHub에서 전달되는 훅(Hook)을 통해서 Pull Request 이벤트가 발생되었을 때 해당 Pull Request를 감지하여 자동 빌드 및 테스트 자동화 시스템을 구성할 수 있기 지원하고 있습니다. 
즉, GitHub에 Pull Request가 생성되면 그 이벤트를 Jenkins에 전달하고, 
Jenkins에서는 해당 payload를 분석하여 해당 PR(Pull Request)에 대한 일련의 과정을 처리하고 그 결과를 다시 GitHub쪽에 전달하는 방식입니다. 


이 자동화 시스템의 장점이라고 한다면, 컴파일 에러 또는 링크 에러를 유발하는 Pull Request가 target branch(대상 브렌치)에 머지되는 것을 막을 수 있는 장점이 있습니다. 
또한 빌드 테스트 외에도 테스트 자동화 시스템을 구축해두면, TC(테스트 케이스)에 따라서 일련의 테스트 과정을 거친 후에 그 결과를 GitHub에 자동으로 리포팅하므로 어느정도 동작성이 검증된 소스 코드가 target branch에 머지되는 : 
   

문제의 상황 기술
---

   
회사에서 GitHub와 Jenkins와 SonarQube 시스템을 연동하여 빌드 및 테스트 자동화 환경을 구축해서 잘 운영하던 중이었습니다. 
최근에 서버를 옮기면서 기존에 잘 되던 GitHub Pull Request Builder 기능이 제대로 동작하지 않는 문제가 발생하였습니다.  
GitHub에서는 Hook이 정상적으로 전송이 되고 Jenkins 서버로부터 정상적으로 응답을 받은 것으로 표시되고 있어서 문제의 원인이 Jenkins-side에 있다고 생각을 했습니다. 


결정적 단서 : 역방향 프록시 설정 오류
---

   
젠킨스 설정에 들어가서 설정이 올바른지 확인하는 도중에 "역방향 프록시 설정 오류"라는 메시지가 눈에 들어왔습니다. 
이것이 GitHub Pull Request Builder가 제대로 동작하지 못하게 하는 원인이라는 의심이 강하게 들었습니다. 


해결 방법 : Jenkins 설정에서 URL 설정
---


아래 메뉴로 들어가서 Jenkins URL 설정을 살펴봅니다. 


- Jenkins 관리
  - 시스템 설정
    - Jenkins URL


제 경우는 위의 주소가 올바르지 않아서 발생하였습니다. 
서버 이전하기 전의 IP를 삭제하고, 새로운 서버의 IP로 설정해줬더니 
Pull Requester Build가 동작하지 않는 문제가 깔끔하게 해결되었습니다. 


만약 URL 주소가 <code>http://localhost:8080/</code>으로 되어 있는 경우에도 
역방향 프록시 오류를 유발할 수 있으므로 
반드시 Jenkins 서버의 URL을 올바르게 입력해주시기 바랍니다. 

