---
title: 워드프레스의 xmlrpc API 이용 방법
permalink: /013_wordpress/001-wordpress-xmlrpc-api.html
description: 워드프레스 자동화 방법 중의 하나인 xmlrpc API 이용 방법에 대해서 설명합니다.
category: wordpress
---
많은 웹페이지들이 워드프레스로 만들어지고 있습니다. 
또한, 네이버 블로그나 티스토리 같은 블로그들을 이용하던 분들 역시도 
워드프레스로 많이 넘어가는 것 같습니다. 


워드프레스의 강점들을 상당히 많습니다. 
손쉽게 적용하고 사용할 수 있는 다양한 플러그인도 훌륭하고, 
웹페이지를 자동화할 수 있는 API 역시도 활용도가 높습니다. 


본 페이지에서는 워드프레스의 xmlrpc API를 이용하는 방법에 대해서 설명합니다.


### 워드프레스 XML-RPC API 페이지


워드프레스의 XML-RPC API에 대해서 가장 잘 정리된 페이지는 
[https://codex.wordpress.org/XML-RPC_WordPress_API](https://codex.wordpress.org/XML-RPC_WordPress_API)로 접속하시면 됩니다. 


사실 XML-RPC는 워드프레스의 취약점 중의 하나입니다만, 
여러가지 플러그인들을 이용해서 그런 취약점을 보완할 수 있습니다. 
잘만 사용한다면 웹페이지 또는 블로그의 자동화를 이뤄낼 수 있습니다. 


워드프레스의 또 다른 단점이라면, 제법 무겁게 동작한다는 것입니다. 
이 때문에 워드프레스 편집기로 웹페이지를 편집할 때 
상당히 버벅거리는 현상을 느낄 수 있습니다. 


XML-RPC API를 통해서 웹페이지를 생성하고 편집하면 
이런 단점을 보완할 수 있는 훌륭한 수단이 됩니다. 


### 포스트 글 가져오는 예제


우선 가장 간단하게 해볼 수 있는 getPost query를 수행해보겠습니다. 
모든 API는 정해진 문서에서 정의한 프로토콜대로 수행해야 합니다. 
우선 getPost 쿼리의 파라미터를 살펴보겠습니다. 


#### 1. getPost 파라미터


|Parameter|Type|Mandotory|Description|
|--|--|--|--|
|username|string| Y | 워드프레스 ID |
|password|string| Y | 워드프레스 비밀번호 |
|post_id|int| Y | 워드프레스 글 번호 |
|fields|array|    |   |



#### 2. Query를 위한 xml 작성


위와 같은 포맷으로 xml을 먼저 생성합니다. 


```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>wp.getPost</methodName>
  <params>
    <param>
      <value><string>id</string></value>
    </param>
    <param>
      <value><string>password</string></value>
    </param>
    <param>
      <value><int>0</int></value>
    </param>
  </params>
</methodCall>
```


필수적으로 입력해야 하는 id, password, 글번호 3개 항목만 포함시켜서 
위와 같이 xml을 생성합니다. 


만약 스크립트가 GitHub와 같은 형상관리 시스템을 이용하고 있다면, 
스크립트에 계정 정보가 포함되지 않도록 유의하시기 바랍니다. 


#### curl 명령을 통해서 query 전송


위와 같이 xml 파일을 생성했다면 curl 명령을 통해서 워드프레스에 전송합니다.


```bash
curl --data @getPost.xml https://웹서버주소/api/xmlrpc
```


위의 query에 대한 응답으로 워드프레스의 글이 리턴됩니다. 


#### PHP의 XML 확장이 가능하지 않습니다?


만약 워드프레스에 아래와 같은 에러가 발생하고, 
포스트 정보를 제대로 가져올 수 없다면 
Query를 전송한 URL을 다시 한번 살펴보시기 바랍니다. 


- 올바른 URL : <code>curl --data @getPost.xml https://웹서버주소/api/xmlrpc</code>
- 잘못된 URL : <code>curl --data @getPost.xml https://웹서버주소/xmlrpc.php</code>


이상으로 워드프레스의 XML RPC를 이용해서 
간단한 query를 진행하는 방법에 대한 설명을 마칩니다. 


이상입니다. 
