Ubuntu Linux Crontab 실행 안됨 (crontab에서는 bash 문법 허용 안됨)
===
   
리눅스에서 주기적으로 어떤 동작이나 작업을 수행시키고 싶을 때 
우리는 crontab을 사용합니다. 
bash 쉘에서는 잘 동작하던 스크립트가 crontab에만 등록하면 
제대로 동작하지 않아서 애를 먹었던 적이 있었습니다. 
쉘에서는 잘 동작하는데 crontab에서는 동작하지 않으면 많이 답답하더군요.   
   
결론부터 말씀드리자면, bash 쉘에서의 문법이 crontab에서는 지원되지 않아서 발생한는 문제가 많습니다. 
본 페이지에서는 쉘에서는 잘 동작하는 스크립트가 crontab에 등록하면 동작하지 않는 문제에 대해서 살펴보고 기록합니다.   
   
crontab에 pushd 명령과 popd 명령을 사용해서는 안됨
---
   
기본적으로 Ubuntu Linux에서 터미널을 열면 쉘이 실행됩니다. 
대부분은 bash 쉘을 사용하지요. 
그래서 crontab에 등록할때도 아래와 같이 입력하는 실수를 범할 수 있습니다.   
   
```bash
15 * * * * pushd ~/project/crontab/boyinblue.github.io/build;./auto.sh ;popd
45 * * * * pushd ~/project/crontab/blog_automation;./auto.sh ;popd
30 * * * * pushd ~/project/crontab/raspberry/get_public_ip;./get_public_ip.sh;popd
```
   
사실 이게 실수라는 것을 인지하기는 쉽지 않습니다. 
SW 개발자로 일하면서 간혹 문제점을 야기하는데 
한 가지 원인은 어이없는 실수이고, 
나머지 원인은 무지에서 비롯된 것이 많습니다.   
   
이 경우는 무지에서 비롯된 문제입니다. 
왜냐하면 pushd 명령과 popd 명령은 bash 쉘에서만 사용할 수 있는 문법으로, 
crontab에서는 이를 인식할 수 없기 때문입니다.   
   
위의 명령을 아래와 같이 수정하면 깔끔하게 해결됩니다.   
   
```bash
15 * * * * cd ~/project/crontab/boyinblue.github.io/build; ./auto.sh
45 * * * * cd ~/project/crontab/blog_automation; ./auto.sh
30 * * * * cd ~/project/crontab/raspberry/get_public_ip; ./get_public_ip.sh
```
   
pushd 명령을 cd로 변경하면 그 이후부터는 의도한대로 동작하는 것을 확인할 수 있습니다.   
   
crontab이 제대로 동작하지 않을 때 원인 분석 방법
---
   
위의 문제는 한 가지 예시에 불과합니다. 
지원하지 않는 pushd 명령을 사용하는 것 외에도 다양한 원인들이 있을 수 있겠지요. 
첫 단계로 시도해볼 수 있는 것은 로그를 수집하는 것입니다. 
하지만 이것은 좋은 방식이면서도 좋지 않은 방식입니다.   
   
아래와 같이 crontab 실행시에 로그를 남기도록 하는 시도는 제대로 동작하지 않을 수 있습니다.   
   
```
0 * * * * pushd abc >> /tmp/error.txt ; ./a.out >> /tmp/error.txt
```
   
위와 같이 수행 결과를 로그로 남기는 것도 가능합니다만, 
표준 출력만 파일에 기록되기 때문에 표준 에러는 로그 파일에 기록되지 않지요.   
   
한 줄로 입력하는 crontab에 로그를 남기는 동작까지 넣는다는 것은 아주 성가신 일이겠지요. 
그래서 발견한 깔끔한 방법이 있습니다.   
   
그것은 바로 crontab의 수행 결과를 이메일로 수신하는 것입니다.   
   
crontab 수행시 문제가 발생할 경우 이메일로 수신하는 방법
---
   
PC에 SMTP 설정을 해두면 crontab 수행시에 에러가 발생할 경우 이메일로 자동 리포팅 됩니다. 
제가 crontab에서 pushd 명령을 사용해서 문제가 되었을 것을 찾게된 것도 
해당 로그가 이메일로 전송되었기 때문에 알 수 있었던 것입니다.   
   
```
root
오전 10:00 (29분 전)
/bin/sh: 1: pushd: not found /bin/sh: 1: ./auto.sh: not found /bin/sh: 1: popd: not found
```
   
위와 같이 pushd 명령이 not found 에러를 리턴하면서 실패를 했고, 
당연히 경로가 맞지 않아서 그 뒤의 명령들이 줄줄이 실패되는 악순환이 발생했지요.
   
SMTP 설정을 통해서 crontab 실패시의 로그를 수신하는 방법
---
   
그렇다면 crontab 실패시의 로그를 이메일로 수신하게 하려면 어떻게 해야 할까요? 
ssmtp 패키지를 설치하고 SMTP 설정을 해주면 됩니다.   
   
관련된 내용은 아래의 제 글을 참고하시기 바랍니다.   
[Ubuntu Linux에서 ssmtp로 이메일 전송하는 초간단 방법](https://boyinblue.github.io/008_ubuntu/001.html)
   
결론
---
   
본 페이지에서는 crontab에서 지원되지 않는 pushd 명령 때문에 crontab이 제대로 수행되지 않은 문제에 대해서 살펴보았습니다. 
   
또한, crontab이 수행되지 않을 때 문제의 원인을 파악하기 위해서는 SMTP 설정을 해주면 쉽게 원인을 파악할 수 있다는 것에 대해서도 언급하였습니다.   

이상입니다.   
