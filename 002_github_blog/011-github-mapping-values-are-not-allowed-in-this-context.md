---
Title: '\"mapping values are not allwed in this context at line 2 column 33\" 해결 방법'
Description: 'GitHub Pages의 md 파일 상단에 YAML 형식의 헤더를 추가했을 때 발생하는 \"mapping values are not allwed in this context at line 2 column 33\"에러를 조치하는 방법에 대해서 설명한다.'
---

지난 시간에 GitHub Pages가 더 잘 검색되도록 하기 위해서 
md 파일의 상단에 아래와 같은 형식으로 title과 description의 YAML 형식의 헤더를 추가하는 방법에 대해서 언급했다.


```
---
Title: 제목으로 사용할 문자열
Description: 페이지에 대한 설명으로 사용할 문자열
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
Title: "mapping values are not allwed in this context at line 2 column 33" 해
결 방법
---
```


<code>\"</code>를 <code>\\\"</code>로 바꾸면 이 문제가 해결된다.


```
---
Title: \"mapping values are not allwed in this context at line 2 column 33\" 해
결 방법
---
```


또한 전체 내용을 작은 따옴표 안에 인용하는 것도 하나의 방법이다. 
단, 작은 따옴표(') 안에 넣는 내용에 작언 따옴표(')가 있어서는 안된다.


문제점을 수정하고 push 하면 정상적으로 빌드 및 발행이 되는 것을 확인할 수 있다. 


결론
---


만약 GitHub Pages의 헤더에 작성하는 YAML 형식의 정보에서 "mapping value are not allowed in this context at line 2 column 33"과 같은 에러가 빌드시에 발생한다면 값에 따옴표가 있는건 아닌지 살펴보자. 



