---
title: GitHub Pages 포스트 읽는데 걸리는 시간 표시하는 방법
description: 깃허브 페이지에서 단어수를 체크해서 글을 읽는데 필요한 예상 시간 계산 방법
category: github-pages
image: /assets/images/github-pages/logo.png
---

요즘 잘 작성된 글들은 글을 읽는데 걸리는 예상 시간을 같이 표기하곤 한다. 
처음에는 이것이 실제 사용자가 글을 읽는데 걸리는 시간을 측정한 통계 데이터이줄 알았다. 
오늘 우연한 기회로 이것이 어떻게 구현되었는지 알게 되었는데 생각보다 간단하게 구현되어 있었다. 

글을 읽는데 소요되는 시간 예상 방법
---

GitHub Pages로 작성된 포스트를 읽는데 걸리는 시간을 계산하는 공식은 아래와 같다. 

> 글을 읽는데 걸리는 시간 = 단어수 / 5단어 / 60초

1초에 5단어씩 읽는다고 가정하면 1초동안 5단어를 읽을 수 있다. 
1분은 60초이므로 1분에 300단어를 읽을 수 있다. 
즉, 단어수를 300으로 나누면 그 글을 읽는데 걸리는 시간을 계산할 수 있다. 


예제
--- 

```
{% raw %}
{% capture count_words %}{{ page.content | number_of_words }}{% endcapture %}
{% capture time_words %}{{ count_words | divided_by: 5 }}{% endcapture %}
- 단어수 : {{ count_words }}
- 읽는데 걸리는 시간 : ~ {{ time_words | diided_by: 60 }} 분
{% endraw %}
```

결과
---

{% capture count_words %}{{ page.content | number_of_words }}{% endcapture %}
{% capture time_words %}{{ count_words | divided_by: 5 }}{% endcapture %}
- 단어수 : {{ count_words }}
- 읽는데 걸리는 시간 : ~ {{ time_words | diided_by: 60 }} 분