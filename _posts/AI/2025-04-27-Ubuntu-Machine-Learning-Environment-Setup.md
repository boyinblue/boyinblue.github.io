---
title: 우분투 머신러닝 개발 환경 설정 방법 (nVIDIA Driver, CUDA, PyTorch 등)
description: 
category: AI
---


우분투 머신러닝 개발 환경
---


우분투에서 머신러닝을 위한 개발 환경을 설정하자. 


|항목|내용|
|---|---|
|Python3|   |
|Visual Studio Code|   |
|NVIDIA Driver|   |
|NVIDIA CUDA|   |
|PyTorch|   |

### 파이썬 설치

머신러닝을 꼭 파이썬으로 수행해야 될 이유는 없어보이지만 
알고있는 거의 모든 개발자들이 파이썬을 이용하여 머신러닝 혹은 딥러닝을 수행합니다. 
아래 명령으로 파이썬을 설치합니다. 

```
# sudo apt-get install python3
```

### Visual Studio Code

VI 편집기를 이용해서 파이썬 스크립트를 수정할 수 있지만, 
Visual Studio Code와 같은 편집기를 이용하면 소스 코드 작성 및 수정이 훨씬 수월합니다. 
특히 Copilot extention을 사용하면 스크립트 작성하는데 걸리는 시간을 상당히 줄일 수 있습니다. 

Visual Studio Code 설치하는 방법은 본 페이지에서는 생략하겠습니다. 

### NVIDIA 드라이버 확인 방법

머신러닝을 위해서는 대규모의 행렬 연산을 수행해야 합니다. 
CPU보다 GPU가 훨씬 빠릅니다. (경우에 따라서 다르지만 약 3배 정도 빠릅니다.)
GPU가 없더라도 머신러닝을 할 수는 있지만 파라미터가 많은 복잡한 연산은 아예 불가할 수 있습니다.  

```
# nvidia-smi
```

터미널에서 nvidia-smi 명령을 입력하면 GPU 모델, 드라이버, CUDA 버전 등을 확인할 수 있습니다. 

### GPU Turn On 방법

nvidia-smi 명령으로 확인해보면 GPU가 Off인 상태가 있습니다.
이때는 아래 명령으로 GPU를 On 시킬 수 있습니다.

```
# nvidia-smi -pm 1
```

nvidia-smi 명령 사용법을 알아보려면 man 명령을 입력하면 됩니다.

```
# man nvidia-smi
```

### PyTorch 설치
학습에 필요한 행렬 연산을 손쉽게 해줍니다. 

```
# pip install pytorch
```

### 개발 환경 테스트
아래 스크립트를 이용하면 정상적으로 개발 환경이 설정되었는지 확인할 수 있습니다.

```
#!/usr/bin/env python3

import torch

print(torch.coda.is_available())
print(torch.version.cuda)
print(torch.backends.cudnn.version())
```


개발 환경 설정 관련 명령어들
---

|내용|명령어|
|---|---|
|nvidia-smi|