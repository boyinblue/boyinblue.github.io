---
title: 링크 프리뷰 구현하는 방법(float 스타일 사용)
permalink: /html/html-horizontal-objects-with-float-style.html
description: 티스토리 블로그에 다른 게시물 링크의 이미지 및 내용이 미리 표시되는 것처럼 프리뷰를 구현하는 방법 설명
image: /assets/images/html-float.png
category: html
---

티스토리 링크 프리뷰
---


티스토리 블로그에 다른 게시물 링크를 걸게 되면, 
위의 그림처럼 대표 이미지와 내용이 미리 표시된다.
GitHub Pages로도 이와 유사한 기능을 사용할 수 있다. 


예제
---


```html
<div style="height: 300; border: 1px dashed; border-radius: 3px;">
  <div style="width: 20%; float: left; margin: 2px; height: 100%">
    <img style="border-radius: 20px;" src="/assets/logo.png" width=100%>
  </div>

  <div style="float: right; margin: 10px 0 10px 0; width: 75%; height: 100%">
    <h3>VS Code 단축키 설명</h3>
    소스코드 편집 스킬을 향상시켜줄 단축키들 설명<br>
    (2022-10-24 작성)<br>
    <a href="/vscode/vs-code-shortcuts.html">더보기</a>
  </div>

  <div style="clear: both; width: 0">
  </div>
</div>
```


>여러 종류의 객체를 가로로 나란히 출력하기 위해서는 <code>float: left;</code> 테그를 사용하면 된다.
>해당 속성을 해제하기 위해서는 <code>clear: both;</code> 구문을 입력하면 된다. 



