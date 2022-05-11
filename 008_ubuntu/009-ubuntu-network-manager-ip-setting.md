---
title: 우분투 리눅스에서 NetworkManager로 IP 설정 방법
description: 우분투 리눅스에서 IP를 설정하는 방법은 3가지가 있습니다. 그 중에서도 NetworkManager로 IP를 설정하는 방법에 대해서 설명합니다.
---


우분투 리눅스에서는 아이피를 설정하는 방법이 3가지가 있습니다. 
그 중에서도 NetworkManager로 IP를 설정하는 방법에 대해서 설명합니다. 


우분투 리눅스에서 NetworkManager로 IP 설정 방법
===


가장 기본이되는 IP 설정 방법은 netplan 입니다. 
만약 netplan이 아닌 NetworkManager로 IP를 설정하기 위해서는
netplan 설정파일 수정이 필요합니다.


```bash
$ sudo vi /etc/netplan/01-network-manager-all.yaml
```


아래와 같이 설정해줍니다.


```
# Let NetworkManager manage all devices on this system
network:
  version: 2
  renderer: NetworkManager
```




