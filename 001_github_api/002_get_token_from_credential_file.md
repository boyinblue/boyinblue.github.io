---
title: GitHub API .git-credentials 파일로부터 id와 token을 안전하게 파싱하는 방법
description: Bash 쉘 스크립트 및 파이썬 스크립트를 이용하여 GitHub 토큰를 파싱하는 방법을 설명합니다.
---


[GitHub API] .git-credentials 파일로부터 id와 token을 안전하게 파싱하는 방법
===
   

GitHub API를 사용하기 위해서는 인증 과정이 필요합니다. 
깃헙에서 토큰을 발급받아서 서버와 통신하는 방식은 SW 개발자들 사이에서 널리 사용되고 있습니다. 
credential을 저장할 수 있도록 설정해두면 ID와 token을 매번 입력하지 않아도 되어 편리합니다. 


이 때 토큰은 홈 디렉토리 내에 <code>.git-credentials</code> 파일에 저장되고, 필요시 해당 파일을 파싱하여 GitHub API 통신시에 활용하면 편리합니다. 
   

본 페이지에서 다루는 내용
---


본 페이지에서는 아래 내용을 기술합니다.   
1. git config 명령을 통해 token을 홈 디렉토리에 저장하는 방법
2. .git-credentials 파일을 파싱하여 id와 token 값을 가져오는 방법
   

작성 환경
---


본 페이지의 내용은 ubuntu OS의 bash script를 기준으로 설명드리는 점을 미리 밝혀둡니다. 
1. OS : Ubuntu OS 
2. Language : Bash Shell Script, Python


토큰을 홈 디렉토리에 저장하는 방법
---
   

서두에서 언급했듯 인증 정보를 홈 디렉토리에 저장해두면 매번 인증 정보를 입력할 필요가 없어서 편리합니다. 
아래의 명령을 통해서 인증 정보가 홈 디렉토리에 저장되도록 설정되었는지 살펴봅니다.   
   

<pre><code>
$ git config --global -l
user.name=boyinblue
user.email=boyinblue@naver.com
credential.helper=store
</code></pre>   


위와 같이 'git config --global -l' 명령을 입력했을 때 *credential.helper=store* 가 출력되면 인증 정보를 홈 디렉토리에 저장하는 것으로 설정되었다는 것을 의미합니다. 또 다른 방법으로는 홈 디렉토리 내부의 .gitconfig 파일을 출력해보는 방법도 있습니다.   


<pre><code>
$ cat ~/.gitconfig
[user]
	email = boyinblue@naver.com
	name = boyinblue
[credential]
	helper = store
</code></pre>   
   

출력 결과를 살펴보면 위와 같이 credential 카테고리의 helper 항목이 store 로 설정되어 있는 것을 알 수 있습니다.   
   

토큰을 홈 디렉토리에 저장하는 명령은 아래와 같습니다. 
이미 토큰이 홈 디렉토리에 저장되도록 설정해두셨을 경우는 아래의 과정을 생략하시면 됩니다.   


<pre><code>
$ git config --global credential.helper store
</code></pre>   
   

위와 같이 입력한 이후에  *git pull* 또는 *git push* 같은 명령을 입력하고 인증 정보를 입력하면 아래와 같이 홈 디렉토리에 .git-credentials 라는 파일이 생성됩니다.   
   
<pre><code>
$ ls ~/.git-credentials -all
-rw------- 1 parksejin parksejin 70  3월  6 17:19 /home/parksejin/.git-credentials
</code></pre>   
   

위와 같이 0600 권한으로 .git-credentials 파일이 생성된 것을 확인하실 수 있습니다. 
파일의 소유자만 읽기와 쓰기 권한이 부여되어 있어서 다른 사용자는 이 파일에 대한 권한이 없습니다. 
심지어 같은 그룹에 있는 사용자도 파일을 확인할 수 없습니다. 


*단, root 권한을 가진 사용자는 해당 파일을 볼 수 있는 방법이 있기 때문에 이 점에 유의하시기 바랍니다.*   


<pre><code>
$ ls ~/.git-credentials 
https://boyinblue:\*******************@github.com
</code></pre>   


저장되는 형식은 https://{id}:{token}@github.com 형식으로 저장이 됩니다. 
GitHub API를 호출하기 위한 토큰을 위의 파일에서 파싱해서 사용하면 됩니다. 


.git-credentials 파일로부터 토큰을 파싱하는 방법
---


그럼 지금부터 .git-credentials 파일로부터 토큰을 파싱하는 방법을 설명하겠습니다. 
토큰 값은 노출되어서는 안되기 때문에 스크립트나 별도의 파일에 저장되지 않도록 각별히 유의하시기 바랍니다. 
특히, 토큰값이 포함된 파일이 GitHub에 commit 되는 순간 해당 토큰은 보안 이슈로 즉각 파기되어 사용할 수 없습니다. 


<pre><code>
#!/bin/bash
credential=$(cat ~/.git-credentials)
credential=${credential##https://}
credential=${credential%%@\*}

id=${credential%%:*}
token=${credential##*:}

echo "ID : ${id}"
echo "token : ${token}"
</code></pre>
   

위의 짧은 bash script는 .git-credentials 파일로부터 id와 token을 파싱합니다. 
최초에 가져온 인증 정보는 "https://{id}:{token}@github.com" 형식입니다.   


직접 입력이 불편하신 분들을 위해서 아래의 GitHub에 업데이트했습니다.   
[get\_token\_from\_credential.sh](https://raw.githubusercontent.com/boyinblue/blog_automation/main/get_token_from_credential.sh "get_token_from_credential.sh")
   

다운로드가 번거로우신 분들은 아래와 같이 wget 명령을 통해서 해당 스크립트를 손쉽게 다운로드 하실 수 있습니다.   
   

<pre><code>
$ wget https://raw.githubusercontent.com/boyinblue/blog_automation/main/get_token_from_credential.sh
</code></pre>


get_token_from_credential.sh 파일에 대한 설명을 드리겠습니다. 


<pre><code>
credential=$(cat ~/.git-credentials)
credential=${credential##https://}
credential=${credential%%@\*}
</code></pre>
   

가장 먼저 "https://" 부분을 제거한 후, '@' 부터의 부분을 제거합니다. 
이 과정이 끝나면 credential 변수에 인증정보가 "{id}:{token}" 형식으로 저장됩니다.   
   

<pre><code>
id=${credential%%:*}
token=${credential##*:}
</code></pre>   
   

위의 명령을 통해서 id 변수에는 ':' 이전의 id 값이 저장되고, 
token 변수에는 ':' 이후의 token 값만 추출되어 저장됩니다.   
   

<pre><code>
$ ./get_token_from_credential.sh 
ID : boyinblue
token : ************
</code></pre>   
   

수행한 결과를 보면 ID와 token 값이 정상적으로 파싱된 것을 확인하실 수 있습니다. 
해당 id 변수와 token 변수를 이용하여 curl 명령을 수행하여 GitHub API를 호출하면 됩니다.   


.git-credentials 파일로부터 토큰을 파싱하는 방법 (파이썬 스크립트)
---


이번에는 추가적으로 파이썬 스크립트를 이용해서 토큰을 가져오는 방법을 
추가로 설명드리겠습니다.


우선 예제부터 나갑니다.


```python
import os

# 홈 디렉토리 경로 가져와서 토큰 파일 경로명 구하기
home_dir = os.path.expanduser('~')
token_file = "{}/.git-credentials".format(home_dir)

# 토큰 파일이 존재하지 않는 경우 예외 처리
if not os.path.exists(token_file):
    print("Token File Not exists :", token_file)
    exit

# 토큰 파일 열기
fp = open(token_file, 'r')

# 라인 파싱하기
lines = fp.readlines()

for line in lines:
    # "https://"로 시작하는 부분 제거
    # 기존 : https://{user}:{token}@github.com
    # 변경 : {user}:{token}@github.com
    line = line.replace("https://", "")

    # '@' 이하 부분 제거
    # 기존 : {user}:{token}@github.com
    # 변경 : {user}:{token}
    idx = line.index('@')
    line = line[0:idx]

    # username 가져오기
    idx = line.index(':')
    github_user = line[0:idx]
    github_token = line[idx+1:]

    # 출력하기
    print("github_user :", github_user)
    print("github_token :", github_token)
```


[예제 다운로드](004-get-token.py)


위의 예제는 아래와 같은 순서로 구성되어 있습니다. 


1. 홈 디렉토리 가져오기
2. 홈 디렉토리 경로를 통해서 토큰 파일 경로 구하기
3. 토큰 파일 존재 여부 확인
4. 토큰 파일 내용 로드
5. username와 token 파싱하기


### 필요한 패키지


<code>import os</code>


홈 디렉토리 경로를 가져오고, 토큰 파일 존재 여부를 확인하기 위해서 
os 패키지를 import 시켜야 합니다. 


### 토큰 파일 경로 구하기


``` python
home_dir = os.path.expanduser('~')
token_file = "{}/.git-credentials".format(home_dir)
```


<code>os.path.expanduser('~')</code> 구문을 통해서 
홈 디렉토리의 경로를 가져옵니다. 


파이썬은 홈 디렉토리를 의미하는 <code>~</code> 경로를 
그대로 사용할 수 없기 때문에 이 과정을 거쳐야 합니다. 


즉, Bash에서는 허용되는 <code>~/.git-credentials</code> 대신에, 
<code>/home/username/.get-credentials</code>와 같이 절대 경로를 사용해야 합니다. 


이유는 파이썬 언어는 여러 OS에서 실행할 수 있어야 하기 때문에 
특정 OS에서만 사용하는 (즉, OS 종속적인) 예외를 허용하지 않으려는 것으로 보입니다. 


### 토큰 파일 존재 확인


```python
if not os.path.exists(token_file):
    print("Token File Not exists :", token_file)
    exit
```


토큰 파일이 존재하는지 체크가 필요합니다. 
credential 정보를 파일로 저장하지 않으면 에러가 발생하기 때문입니다. 


### 토큰 파일 읽어오기


```python
fp = open(token_file, 'r')
lines = fp.readlines()
```


토큰 파일로부터 크레덴셜 정보를 모두 가져옵니다.
대부분의 경우는 크레덴셜 정보가 하나 뿐이지만, 
여러 프로젝트를 진행할 경우 다수의 깃헙 서버의 크레덴셜 정보가 
하나의 파일에 누적 저장될 수 있기 때문입니다. 


### 토큰 파일 파싱


```python
for line in lines:
    # "https://"로 시작하는 부분 제거
    # 기존 : https://{user}:{token}@github.com
    # 변경 : {user}:{token}@github.com
    line = line.replace("https://", "")

    # '@' 이하 부분 제거
    # 기존 : {user}:{token}@github.com
    # 변경 : {user}:{token}
    idx = line.index('@')
    line = line[0:idx]

    # username 가져오기
    idx = line.index(':')
    github_user = line[0:idx]
    github_token = line[idx+1:]
```


크레데셜 정보는 "https://{user}:{token}@github.com" 형식으로 저장되기 때문에 
"https://" 부분을 제거하고, "@github.com" 부분을 제거해주고 시작합니다. 


그러면 "{user}:{token}" 형식의 크레덴셜 정보만 남게 됩니다. 
다시 <code>:</code> 앞쪽은 username으로 뒤쪽은 token으로 인식해서 가져오면 
파싱은 모두 완료됩니다. 


결론
---


본 페이지에서는 GitHub의 토큰 정보가 어느 파일에 저장되는지와, 
토큰 정보를 포컬 파일에 저장해두는 방법에 대해서 다루었습니다. 


아울러, 배쉬 스크립트와 파이썬 스크립트로 해당 파일을 
파싱하는 방법에 대해서도 설명드렸습니다. 

   
이상입니다. 




[✔️  GitHub API 호출시 Bad Credentials 에러 발생시 조치 방법](001_bad_credential.html '본 페이지에서는 GitHub API 호출시에 Bad credentials 응답이 오는 문제를 해결하는 방법을 ')
---


본 페이지에서는 GitHub API 호출시에 Bad credentials 응답이 오는 문제를 해결하는 방법을 기술하고자 합니다.


[✔️  server certificate verification failed. CAfile none CRLfile none 에러 조치 방법](003-server-certificate-verification-fail.html 'GitHub 서버로부터 통신을 시도할 때 server certificate verification failed. CAfile none CRLfile none 에러가 발생할 경우 조치하는 방법에 ')
---


GitHub 서버로부터 통신을 시도할 때 server certificate verification failed. CAfile none CRLfile none 에러가 발생할 경우 조치하는 방법에 대해서 설명합니다.


[✔️  GitHub에서 레포지토리의 생성일을 확인하는 방법](004-github-how-to-get-the-creation-date-of-repository.html 'GitHub API를 이용해서 레포지토리의 생성일을 확인하는 방법에 ')
---


GitHub API를 이용해서 레포지토리의 생성일을 확인하는 방법에 대해서 설명합니다.


[✔️  GitHub API](index.html 'GitHub API 사용 방법 및 관련')
---


GitHub API 사용 방법 및 관련 팁을 제공합니다.


[✏️ ](https://www.github.com/boyinblue/boyinblue.github.io/edit/main/001_github_api/002_get_token_from_credential_file.md '수정하기')

