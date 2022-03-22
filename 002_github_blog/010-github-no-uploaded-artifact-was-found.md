---
title: GitHub Pages 빌드 에러 "Error: No uploaded artifact was found! Please check if there are any errors at build step."
description: GitHub Pages에서 빌드 에러가 발생시에 조치하는 방법에 대해서 설명합니다.
---


GitHub Pages 빌드 에러
===


최근에 GitHub Pages를 이용해서 웹페이지를 구성하였고, 
글쓰기의 재미에 푹 빠져있습니다. 
GitHub Pages는 무척 흥미로운 무료 웹서버로 참 매력적인 서비스임에 틀림없습니다. 
새로운 글들을 생산해내는 도중에 생경한 에러를 만나고야 말았습니다.


문제의 상황 파악
---


GitHub Pages에 연결된 레포지토리의 <code>Actions</code>에 빨간불이 떠 있는게 아니겠습니까? 자세히 들어가서 살펴보니 아래와 같은 에러 메시지가 발견됩니다.


```
Error: No uploaded artifact was found! Please check if there are any errors at build step.
```


GitHub Pages에 연결된 레포지토리에 commit 또는 push를 하게되면, 
내부적으로 빌드(Build) 과정을 거쳐서 웹서버에 반영(Deploy)됩니다. 
컨텐츠 중에서 업로드 되지 않은 항목이 있으니, 
빌드 과정에서 에러가 있는지 확인해보라는 메시지입니다.


빌드 로그를 살펴보니 아래와 같은 메시지가 발견됩니다.


```
Error reading file /github/workspace/006_java/001.md: invalid byte sequence in UTF-8 
  Conversion error: Jekyll::Converters::Markdown encountered an error while converting '006_java/001.md':
                    The source text contains invalid characters for the used encoding UTF-8
```


문제가 되는 파일은 <code>/006\_java/001.md</code>라는 파일에서 발생을 했고, 
<code>UTF-8</code>형식으로 처리할 수 없는 문자가 포함되어 있다는 메시지였습니다. 
실제로 해당 파일을 열어보니 파일이 깨져 있었습니다.


문제의 해결
---


문제가 되는 파일을 삭제하고 수정 사항을 push 했더니 
정상적으로 빌드 및 업로드가 된 것을 확인할 수 있었습니다.


결론
---


만약 GitHub Pages에서 빌드 및 업로드 에러가 발생한다면, 
Encoding 형식에 맞지 않는 문자가 *md* 파일에 포함되었는지 확인해보시기 바랍니다.   


파일이 깨져있거나, 처리할 수 없는 문자가 있을 경우 해당 파일을 삭제하고 push하면 정상적으로 빌드되는 것을 확인하실 수 있습니다.



