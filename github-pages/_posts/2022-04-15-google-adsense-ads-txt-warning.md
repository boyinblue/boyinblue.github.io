---
title: 구글 애드센스 ads.txt 문제 해결 방법
permalink: /002_github_blog/014-google-adsense-ads-txt-warning.html
description: 구글 애드센스에서 ads.txt 파일에 문제가 있을 경우 조치 방법
category: github-pages
---


구글 애드센스 ads.txt 문제 해결 방법
===


구글 애드센스에서 ads.txt 파일에 문제가 있을 경우 조치 방법


GitHub Pages에서 ads.txt 파일 생성이 필요한 이유
---


무료 웹서버인 GitHub Pages로 웹서버를 운영한지도 
1개월이 조금 더 지났습니다. 
기존에 운영하던 네이버 블로그와 티스토리 블로그와는 달리 
GitHub Pages는 참 매력적이 점이 많이 있습니다. 


하루에 발행할 수 있는 페이지 수에 제한이 없고, 
이로 인해서 파이썬이나 배쉬와 같은 스크립트를 이용해서 
자동으로 컨텐츠를 생성해 낼 수도 있습니다. 


또한, markdown 문법으로 시원시원하게 웹 페이지를 작성할 수 있습니다. 


많은 강점들을 가지고 있지만, 동시에 여러 단점들도 존재합니다. 


기존에 티스토리 블로그를 운영할 때에는 사이트맵 파일을 생성할 필요도 없고, 
<code>robots.txt</code> 파일이나 <code>ads.txt</code> 같은 파일을 
전혀 신경 쓸 필요가 없었습니다. 


하지만 GitHub Pages에서는 블로그 주인이 이런 파일들을 
모두 신경써서 챙겨줘야 하는 단점이 있습니다. 


문제의 현상
---


![수익 손실 위험 - 수익에 심각한 영향을 미치지 않도록 사이트에서 발견된 ads.txt 파일 문제를 해결해야 합니다.](014-google-adsense-ads-txt-warning.png)


GitHub Pages를 생성한지 약 십여일만에 구글 애드센스 연동이 가능했고, 
티스토리에서 구글 애드센스를 연동했을 때는 경험하지 못한 
생경한 경고 메시지를 만나게 되었습니다. 


구글 애드센스 페이지에 접속하면 "수익 손실 위험 - 수익에 심각한 영향을 미치지 않도록 사이트에서 발견된 ads.txt 파일 문제를 해결해야 합니다."라는 경고 메시지가 떴습니다. 


문제의 원인
---


웹 페이지의 루트 디렉토리에 <code>ads.txt</code> 파일이 존재하지 않아서 발생한 문제입니다. 


조치 방법
---


웹 페이지의 루트 디렉토리에 <code>ads.txt</code> 파일을 생성하고, 
파일 안에 아래와 같은 형식으로 입력해주면 됩니다. 


```
google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, XXXXXXXXXXXXXXXX
```


참고로 <code>ads.txt</code> 파일에 포함되어야 할 내용은 
구글 애드센스에서 친절하게 제공합니다. 


문제 해결 확인
---


위와 같이 웹 페이지의 루트 디렉토리에 <code>ads.txt</code> 파일을 
구글 애드센스에서 가이드한 포맷으로 작성해줬더니 문제가 해결되었습니다. 


그리고 지금 아주 미미하지만 구글 애드센스 수익이 발생하기 시작했습니다. 


결론
---


구글 애드센스에서 <code>ads.txt</code> 파일 관련 경고 메시지가 뜨면, 
구글 애드센스에서 제공하는 <code>ads.txt</code> 파일을 
웹 페이지의 루트 디렉토리에 업로드해주면 깔끔하게 해결됩니다. 


[✏️ ](https://www.github.com/boyinblue/boyinblue.github.io/edit/main/002_github_blog/014-google-adsense-ads-txt-warning.md '수정하기')
