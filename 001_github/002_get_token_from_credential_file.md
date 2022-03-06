[GitHub API] .git-credentials 파일로부터 id와 token을 안전하게 파싱하는 방법
===
   
GitHub API를 사용하기 위해서는 인증 과정이 필요합니다. 
토큰을 발급받아서 통신하는 방식은 SW 개발자들 사이에서 널리 사용되고 있습니다. 
credential을 저장할 수 있도록 설정해두면 ID와 token을 매번 입력하지 않아도 되어 편리합니다. 
이 때 토큰은 홈 디렉토리 내에 .git-credentials 파일에 저장되고, 필요시 해당 파일을 파싱하여 GitHub API 통신시에 활용하면 편리합니다. 
   
본 페이지에서는 아래 내용을 기술합니다.   
1. git config 명령을 통해 token을 홈 디렉토리에 저장하는 방법
2. .git-credentials 파일을 파싱하여 id와 token 값을 가져오는 방법
   
   
토큰을 홈 디렉토리에 저장하는 방법
---
   
서두에서 언급했듯 인증 정보를 홈 디렉토리에 저장해두면 매번 인증 정보를 입력할 필요가 없어서 편리합니다. 
아래의 명령을 통해서 인증 정보가 홈 디렉토리에 저장되도록 설정되었는지 살펴봅니다.   
   
'''console
$ git config --global -l
user.name=boyinblue
user.email=boyinblue@naver.com
credential.helper=store
   
위와 같이 'git config --global -l' 명령을 입력ㅎ
