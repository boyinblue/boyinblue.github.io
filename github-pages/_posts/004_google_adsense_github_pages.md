---
title: GitHub 블로그에 구글 애드센스 스크립트 삽입하는 방법 및 삽입 위치
permalink: /002_github_blog/004_google_adsense_github_pages.html
description: GitHub Pages에 구글 애드센스 스크립트를 삽입하는 위치를 설명합니다.
---


GitHub 블로그에 구글 애드센스 스크립트 삽입하는 방법 및 삽입 위치
===
   

무료 웹서버로 활용할 수 있는 GitHub Pages에 블로그를 개설했다면 각종 검색엔진에 사이트를 등록하여 검색으로 인한 유입량을 늘려야 하겠지요. 
더불어, 구글 애드센스를 연동하면 소소하지만 수익을 얻을 수도 있습니다. 
티스토리와 같은 블로그는 직접 스킨을 편집할 수 있는 기능이 있지만, 
GitHub Pages는 막상 어디에 구글 애드센스 스크립트를 삽입해야 하는지 다소 막연할 수 있습니다. 
저도 처음에는 구글 애드센스의 스크립트를 GitHub 블로그의 어디에 삽입해야 하는지 몰라서 다소 난감했습니다. 
결론부터 말씀드리자면, 사용하는 스킨에 따라서 구글 애드센스의 스크립트를 삽입하는 위치가 다를 수 있습니다.   
   
   
GitHub 블로그의 Head Script 위치 확인하는 방법
---
   

GitHub Pages를 처음 개설하면 READMD.md 파일밖에 존재하지 않기 때문에 도대체 어디를 편집해야 하는지 난감할 수 있습니다. 
이 때는 GitHub Pages의 메인 페이지에서 html 소스 보기를 하면 헤더 스크립트 파일을 어디에 작성해야 하는지에 대해서 알 수 있습니다.   
   

![GitHub 애드센스 스크립트 작성 위치](/assets/images/004_google_adsense_script_insert_position.png "GitHub 애드센스 스크립트 작성 위치")
   

HTML 소스보기를 확인해보면 위의 빨간줄로 강조한 부분에 주석으로 커스터마이징 할 수 있는 파일 경로가 표기되어 있습니다.   
   

저는 "jekyll-theme-slate" 테마를 사용하고 있고, 저의 경우는 <code>\_includes/head-custom.html </code> 파일을 생성하면 커스터마이징이 가능합니다. 
이 경로는 스킨에 따라서 다를 수 있기 때문에 반드시 위의 방법(페이지 소스 보기)으로 확인하시기 바랍니다. 
저는 이렇게 확인하지 않고 다른 스킨을 사용하는 블로거의 경로를 따라했다가 시간과 노력을 제법 낭비했습니다. 
부디 제가 공유하는 내용을 꼼꼼히 읽어보시고 시간과 노력을 낭비하시는 일이 없으시길 바랍니다.   
   
   
GitHub Head Script 편집 방법
---
   

위의 방법으로 head snippets 경로를 확인했지만, 실제로 해당 경로에 파일은 존재하지 않습니다. 
<code>head-customer.html</code>라는 파일이 존재하지 않을 뿐더러, 
심지어는 <code>\_include</code> 라는 디렉토리도 존재하지 않습니다. 
   

뭔가 당황스럽지만 실망하기에는 아직 이릅니다. 
해당 파일이 존재하지 않으면 그냥 기존 헤더가 달리게 되고, 
해당 파일이 존재하면 그 내용이 추가로 포함되도록 되어 있습니다. 
해당 경로에다가 html 파일을 생성해주면 됩니다.   
   

<pre><code>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXX"
     crossorigin="anonymous"></script>
</code></pre>
   

<code>\_include/head-customer.html</code> 파일을 위와 같이 편집한 이후에 "페이지 소스보기"를 다시 수행했더니 위의 스크립트가 홈페이지에 제대로 삽입된 것을 확인할 수 있었습니다. 
그 이후에 구글 애드센스에서도 위의 스크립트가 정상적으로 인식이 되는 것을 확인할 수 있었습니다.   
   
   
결론
---
   

GitHub 블로그에서 구글 애드센스 스크립트 삽입하는 위치를 확인하기 위해서는 루트 페이지의 "페이지 소스 보기"를 수행하면 됩니다. 
이 위치는 사용하는 스킨에 따라서 다를 수 있습니다. 
해당 경로에 파일이 없을 경우 당황하지 마시고 해당 파일을 생성하시면 되겠습니다.   

이것으로 GitHub 페이지에 구글 애드센스 스크립트를 삽입하는 방법에 대한 글을 모두 마칩니다. 유용한 정보였기를 바랍니다. 


[✏️ ](https://www.github.com/boyinblue/boyinblue.github.io/edit/main/002_github_blog/004_google_adsense_github_pages.md '수정하기')

