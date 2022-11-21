---
title: 우분투 리눅스에서 sudo 명령시에 루트 비밀번호 입력을 스킵하는 방법
description : How to skip root password during sudo command
category: ubuntu
image: /assets/images/ubuntu/ubuntu-linux-sudo-password-skip.jpg
---

우분투 리눅스를 이용하여 스크립트를 작성하다보면 루트 권한이 필요한 경우가 종종 있다. 
사용자가 로컬에서 직접 실행하는 스크립트라면 귀찮더라도 root 비밀번호를 입력해주면 된다. 
하지만 crontab이나 서비스로 돌고 있는 스크립트에서는 admin 비밀번호를 입력할 수 없다. 
이 때 특정 사용자는 sudo 명령시에 비밀번호를 입력하지 않도록 설정할 수 있다. 


물론 비밀번호 없이 sudo 명령을 수행할 수 있는 것은 위험하다. 
그렇기 때문에 아래 방법은 불가피할 경우에만 제한적으로 사용하기를 권장한다. 


sudo 비밀번호 없이 실행할 수 있도록 설정하는 방법
---
`visudo` 명령을 통해서 권한을 설정할 수 있다. 
이 부분에 대해서는 잘 알고 계실 것이라고 생각하고 바로 설명하겠다. 


```
sudo visudo
```

위의 명령을 통해서 관리자 권한을 편집한다. 

```
# User privilege specification
root ALL=(ALL:ALL) ALL
jenkins ALL=(ALL:ALL) ALL
```

보통은 위와 같이 `jenkins ALL=(ALL:ALL) ALL`로 되어 있다. 
이 부분을 `jenkins ALL=(ALL) NOPASSWORD:ALL`로 수정하면 된다. 


그 이후부터는 `sudo` 명령을 붙여도 비밀번호를 물어보지 않는다. 

