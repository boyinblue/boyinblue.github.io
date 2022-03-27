---
title: '\"mapping values are not allwed in this context at line 2 column 33\" 해결 방법'
description: 'GitHub Pages의 md 파일 상단에 YAML 형식의 헤더를 추가했을 때 발생하는 \"mapping values are not allwed in this context at line 2 column 33\"에러를 조치하는 방법에 대해서 설명한다.'
---


지난 시간에 GitHub Pages가 더 잘 검색되도록 하기 위해서 
md 파일의 상단에 아래와 같은 형식으로 title과 description의 YAML 형식의 헤더를 추가하는 방법에 대해서 언급했다.



```
---
title: 제목으로 사용할 문자열
description: 페이지에 대한 설명으로 사용할 문자열
---
```


위와 같이 GitHub Pages의 md 파일 상단에 해당 내용을 추가하면, 
HTML로 변환된 페이지의 헤더에 Title과 Description 테크가 적절하게 갱신되기 때문에 검색 엔진으로부터 더욱 잘 노출될 가능성이 높다.


하지만 위의 형식으로 입력한 컨텐츠들 중에서 아래와 같은 에러를 띄워서 
빌드시에 경고 메시지로 표시되는 경우가 더러 있다.


```
mapping values are not allowed in this context at line 2 column 33 
```


실제 해당 파일을 찾아가보면 내용에 쌍따옴표(\")가 있어서 발생하는 경우가 많다. 


```
---
title: "mapping values are not allwed in this context at line 2 column 33" 해
결 방법
---
```


<code>\"</code>를 <code>\\\"</code>로 바꾸면 이 문제가 해결된다.


```
---
title: \"mapping values are not allwed in this context at line 2 column 33\" 해
결 방법
---
```


또한 전체 내용을 작은 따옴표 안에 인용하는 것도 하나의 방법이다. 
단, 작은 따옴표(') 안에 넣는 내용에 작언 따옴표(')가 있어서는 안된다.


문제점을 수정하고 push 하면 정상적으로 빌드 및 발행이 되는 것을 확인할 수 있다. 


Invalid scheme format 에러 발생 시 조치 방법
---


Invalid scheme format 에러가 발생할 경우 렌더링을 지원하지 않는 파일 포맷에 의한 것일 수 있다.


```
Error:  Invalid scheme format: '2022-03-23T00'
```


만약 위와 같은 에러가 빌드 과정에서 확인되면, 
파일명에 <code>:</code>가 포함되어 있지는 않은지 확인이 필요하다. 


필자의 경우 자동으로 생성되는 페이지들이 있는데, 
이 파일명에 <code>:</code>가 포함되어 있어서 빌드에 실패했다.


<code>2022-03-23T00:00:00.md</code>와 같이 <code>:</code>가 포함된 부분을 수정했더니, 
정상적으로 빌드가 되는 것을 확인할 수 있었다.


결론
---


만약 GitHub Pages의 헤더에 작성하는 YAML 형식의 정보에서 "mapping value are not allowed in this context at line 2 column 33"과 같은 에러가 빌드시에 발생한다면 값에 따옴표가 있는건 아닌지 살펴보자. 


또한, <code>:</code>와 같은 문자도 허용되지 않기 때문에 주의가 필요하다.



