---
title: 우분투 리눅스에서 펌웨어 업그레이드 방법
description: 2 devices have a firmware upgrade available.
category: ubuntu
image: /assets/images/ubuntu/logo.png
---

ssh를 이용해서 우부투 서버에 접속을 했다. 
아래와 같은 메시지를 발견했다. 


```
2 devices have a firmware upgrade available.
Run 'fwupdmgr get-upgrades' for more information.
```

장치에 업그레이드할 수 있는 새로운 펌웨어가 발행된 것으로 보인다. 
`fwupdmgr get-upgrades` 명령을 통해서 더 많은 정보를 얻을 수 있다고 한다. 


fwupdmgr get-upgrades
---

아래의 명령을 실행해보면 업그레이드 관련된 내용이 잔뜩 표시되기만하고 업그레이드를 할 수는 없다. 

```
$ sudo fwupdmgr get-upgrades
```

업그레이드 명령
---

업그레이드를 위해서는 아래의 명령을 실행하면 된다. 
중간에 <kbd>Y</kbd>나 <kbd>N</kbd> 등을 선택해줘야 한다.

```
$ sudo fwupdmgr update
```

업그레이드가 완료된 이후에 재부팅이 필요할 수 있다. 
