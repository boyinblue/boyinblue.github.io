---
title: OpenCV를 이용하여 이미지를 출력하는 방법과 캠을 동작시키는 방법
permalink: /004_python/001.html
description: OpenCV를 이용해서 이미지를 출력하는 방법과 실시간으로 캠 영상을 표시 방법을 설명합니다.  
category: python
image: /assets/images/python/logo.png
---
Ubuntu Linux와 Python 언어를 기준으로 작성되었습니다.   
   
   
OpenCV를 이용해서 이미지를 출력하는 방법
---

   
아래의 짧은 파이선 스크립트로 'test.png' 파일을 화면에 출력할 수 있다. 
OpenCV를 사용하므로 OpenCV 패키지가 설치되어 있어야 한다.   
   

처음에 화면이 뜨기까지는 시간이 상당히 소요된다. 
사용자로부터 키 입력을 계속 받다가 'q'가 입력되면 프로그램이 종료되는 구조다.   

[예제](https://raw.githubusercontent.com/boyinblue/test/main/python/opencv/opencv.py)


```python
import cv2

if __name__ == '__main__':
    img = cv2.imread('test.png')
    cv2.imshow('window_name', img)

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
```


짧은 스크립트로 이미지 파일을 출력할 수 있다니 놀랍기만 하다. 
하지만 놀라기는 아직 이르다. 
아주 간단한 스크립트 몇 줄로 PC의 카메라도 동작시킬 수 있다.   
   

OpenCV를 이용해서 캠을 동작시키는 방법
---

   
이미지 뿐만 아니라 웹캡도 동작시킬 수 있다. 
이런 프로그램을 윈도우즈에서 C를 이용해서 작성하는 것이 얼마나 어려운 일인지 안다. 
그 어려운 것을 파이선은 이렇게 손쉽게 할 수 있다.   


[예제](https://raw.githubusercontent.com/boyinblue/test/main/python/opencv/opencv2.py)


```python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyWindow('frame')

# When everything done, release the capture
cap.release()
```

   
위와 같이 스크립트를 작성하고 실행하면 진짜로 웹캠이 실행되면서 
내 못생긴 얼굴이 화면에 실시간으로 출력되기 시작한다.   

   
인텔에서 만든 OpenCV로 할 수 있는 것은 무궁무진할 것 같다. 
파이선이라는 놀라운 언어가 지금껏 하기 어려웠던 것들을 손쉽게 할 수 있도록 해준다. 
놀랍고도 놀라울 따름이다.   
