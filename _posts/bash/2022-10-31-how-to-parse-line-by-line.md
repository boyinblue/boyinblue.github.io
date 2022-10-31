---
title: bash에서 라인 단위로 파싱하는 방법 (IFS 구분자 변경)
description: How to parse line by line on Bash
category: bash
image: /assets/images/bash/logo.svg
---

bash 쉘에서 for 구문을 사용하면 공백을 기준으로 구분된다. 
간혹 개행을 기준으로 분리해서 처리가 필요할 때가 있다. 
IFS 구분자를 변경해서 라인별로 처리하는 방법을 설명한다. 


예제
---

```bash
lines=$(curl "https://boyinblue.github.io")

IFS_OLD=$IFS
IFS=$'\n'
for line in ${lines}
do
  echo "${line}"
done
IFS=$IFS_OLD
```

위의 예제를 살펴보면, `IFS_OLD`에 기존 구분자를 저장한 다음에, 
`IFS`에 `$'\n'`을 대입한다. 
그 다음에 다시 `IFS`에 `$IFS_OLD`를 할당한다. 
이렇게 하면 기존에 사용하던 구분자 설정으로 다시 돌아갈 수 있어서 편리하다. 


주의할 점
---

```bash
lines=$(curl "https://boyinblue.github.io")

IFS_OLD=$IFS
IFS=$'\n'
for line in "${lines}"
do
  echo "${line}"
done
IFS=$IFS_OLD
```

for 구문을 돌릴 문자열을 쌍따옴표로 인용하면 
원하는 결과를 얻을 수 없이 `${lines}` 변수 전체가 
하나의 라인으로 인식되기 때문에 원하는 결과를 얻을 수 없다. 


