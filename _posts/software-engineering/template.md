---
title: SW 개발 및 검증에 있어서 shift-left와 shift-right의 의미
description: The meaning of 'shift-left' and 'shift-right'
category: software-engineering
image: /assets/images/software-engineering/IBM-System-Science-Institute-Relative-Cost-of-Fixing-Defects.png
---

사무실에서 업무를 보는 도중에 아래와 같은 문장을 발견했다. 


It will enable you to `shift quality to the left` and help drive faster feedback.


처음에는 관용적으로 사용하는 영어 표현인줄 알았다. 
하지만 구글에서 찾아보니 영어 표현이라보다는 SW 개발 업무를 하는 사람들이 널리 사용하는 표현이었다. 


Shift-left의 뜻
---
![SW 개발 단계별 실패 비용](/assets/images/software-engineering/IBM-System-Science-Institute-Relative-Cost-of-Fixing-Defects.png)
위의 그래프에 힌트가 있다. (출처 : IBM Systems Sciences Institue)
소프트웨어와 제품은 크게 아래 4단계의 라이프 싸이클을 가진다. 

- 디자인
- 구현
- 검증
- 유지보수

아무리 잘 만든 프로그램이나 제품이라고 하더라도 결함이 있기 마련이다. 
그리고 그 결함들은 라이프 싸이클 전 단계에 걸쳐서 지속적으로 검출된다. 
출시 이후에 발견되는 결함의 실패 비용이 100이라고 한다면, 
디자인 단계에서 결함이 발견되면 1만 투입되면 되고, 
구현 단계에서 결함이 발견되면 6.5만 투입되면 되고,
검증 단계에서 결함이 발견되면 15만 투입되면 된다. 


문제는 빨리 발견될수록 저렴한 비용으로 해결할 수 있다는 것이다. 
빨리 문제를 발견하면 그것을 바로잡는데 드는 실패 비용을 절감할 수 있는 것이다. 
shift-left는 디자인, 구현, 검증 단계에서 최대한 많은 문제를 찾아내는 것을 의미한다. 
출시 이후 시장에서 발생하는 문제를 검증단계에서 찾아내서 고치고, 
검증단계에서 발생하는 문제를 구현 단계에서 검출해서 수정하면 더 저렴한 비용으로 문제를 해결할 수 있다. 


Shift-right의 뜻
---
꼭 조기에 문제를 발견해서 해결하는 방법만 있는게 아니다. 
Shift-right도 나름대로의 장점이 있다. 
새로운 기능을 빠르게 구현해서 출시하면 적기에 시장에 출시할 수 있는 장점이 있다. 
고객들의 반응을 살펴보기도 편리하고 사용자 친화적인 것이 특징이다. 


어느 것이 더 좋을까?
---
대부분의 하드웨어 제품들은 shift-left가 중요하다. 
시장에서 문제가 발생할 경우 서비스 비용이 발생한다. 
하드웨어 자체의 결함이 있으면 막대한 비용이 발생한다.

- 하드웨어를 교체해주는데 필요한 부품 비용
- 서비스맨이 내방해서 조치하는데 필요한 비용
- 물류 비용


반면, 소프트웨어 서비스들은 shift-right도 괜찮다. 
문제가 발생하면 재빨리 수정해서 다시 릴리즈하면 된다. 


결론
---
shift-left라는 표현은 거창하거나 어려운 개념이 아니다. 
우리가 이미 소프트웨어 및 제품을 개발하는 과정에서 무의식적으로 힘을 쏟고 있는 부분이다. 
shift-left의 개념은 쉽지만, 이것을 달성하기는 쉽지 않다. 
경험도 필요하고 방법론도 필요하고 시스템도 필요하다. 