---
title: 트위터 카드 검증 사이트에서 Unable to render Card preview 에러 발생
description: Twitter Card Validator에서 GitHub Pages 글 검증시에 Unable to render Card preview 에러가 발생하는 문제
category: github-pages
tags:
- github-pages
- twitter
---

트위터 카드란?
---


웹사이트나 블로그의 운영 목적은 최대한 많은 사람들에게 
콘텐츠를 확산시키기 위함입니다. 
더 많은 트래픽은 더 많은 광고 수익을 의미합니다. 
많은 블로그들이 양질의 콘텐츠 작성을 위해 노력합니다. 
동시에 콘텐츠를 페이스북, 트위터 등의 SNS를 통해 퍼트립니다. 


트위터 카드는 트위터를 통해서 공유되는 페이지의 미리 보기를 제공합니다. 
이를 통해서 사용자는 링크된 페이지의 정보를 직관적이고 빠르게 파악합니다. 
![트위터 카드 예제](/assets/images/github-pages/twitter-card.png)


HTML 메타 테그(Open Graph)
---


트위터 카드는 HTML에 포함된 메타 테그에서 트위터 관련 정보를 이용합니다.  
아래는 HTML 헤더에 포함된 트위터 관련 오픈그래프 정보입니다. 


```html
<meta name="twitter:card" content="summary_large_image" />
<meta property="twitter:image" content="https://boyinblue.github.io/assets/logo.png" />
<meta property="twitter:title" content="현업 SW 개발자의 연구 노트" />
```


<dl>
  <dt>`twitter:card`</dt>
  <dd>트위터 카드에 표시될 형식을 알려줍니다.</dd>
  <dd>`summary_large_image`는 위의 예시처럼 큰 이미지를 이용합니다.</dd>

  <dt>'twitter:image'</dt>
  <dd>트위터 카드에 표시될 이미지를 알려줍니다.</dd>

  <dt>'twitter:title'</dt>
  <dd>트위터 카드에 표시될 제목을 알려줍니다.</dd>
</dl>


트위터 카드 검증 페이지
---


[Twitter Card Validator](https://cards-dev.twitter.com/validator '트위터 카드 검증 페이지)


위의 홈페이지에 접속하셔서 체크할 페이지의 URL을 입력하시면 됩니다. 


트위터 카드 검증 실패
---


![트위터 카드 검증 실패](/assets/images/twitter-card-validator-unable-to-render-card-preview.png)


제가 작성한 페이지를 입력했더니 위의 화면처럼 "Unable to render Card preview"라는 메시지를 토해냅니다. 


[트위터 커뮤니티 관련 글](https://twittercommunity.com/t/unable-to-render-card-preview/173566/42)


해결 방법을 확인하기 위해서 구글에서 `Unable to render Card preview` 키워드로 검색해보니 이와 비슷한 문제로 고생하고 있는 개발자들이 많이 있었습니다. 


해결 방법
---


트위터 카드 검증 사이트에서는 에러가 발생했지만, 
실제로 트위터로 업로드를 해봤더니 정상적으로 트위터 카드가 발행되었습니다. 


![트위터 카드 업로드 오래 걸림](/assets/imagES/unable-to-tweet-with-github-pages.png)


다만, 시간이 오래 걸립니다. 거의 10분을 소요된 것 같습니다. 
위의 화면에서 상당한 지연이 발생한 것을 제외하고는 
큰 문제 없이 트위터 카드를 발행할 수 있었습니다. 


결론
---


트위터 카드 검증 페이지에서 `Unable to render Card preview' 
에러가 발생하더라도 트위터 카드 발행이 가능할 수 있습니다. 
이 부분은 트위터 카드 검증 페이지의 오류로 보입니다. 


이 떄는 트위터 관련 메타 테그가 정상적인지 확인하시고, 
이상이 없다고 생각되면 그냥 트윗을 날리세요. 


트위터 카드 검증 페이지에서 검증 실패하더라도, 
정상적으로 트위터 카드가 발행될 수 있기 때문입니다. 
다만, 시간이 다소 오래 걸려서 인내심이 필요할 수 있습니다. 
