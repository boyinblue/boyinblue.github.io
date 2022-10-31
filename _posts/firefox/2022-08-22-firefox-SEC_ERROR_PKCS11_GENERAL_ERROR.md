---
title: SEC_ERROR_PKCS11_GENERAL_ERROR 에러 발생시 조치 방법
permalink: /022_firefox/001-firefox-SEC_ERROR_PKCS11_GENERAL_ERROR.html
description: Firefox 웹브라우저에서 SEC_ERROR_PKCS11_GENERAL_ERROR 에러가 발생할 경우 조치하는 방법에 대해서 설명합니다.
category: firefox
image: https://user-images.githubusercontent.com/50429025/185848984-01adfb6f-1c44-4de6-8b16-6174ed31d90e.jpg
---

사무실에서 사용하는 Note PC의 웹브라우저로 사내 인트라넷을 접속해보면 "SEC_ERROR_PKCS11_GENERAL_ERROR"라는 에러가 지속적으로 발생하기 시작했습니다. Microsoft Edge, Chrome, Firefox 등을 사용하고 있는데 Chrome은 괜찮은데 유독 Microsoft Edge와 Firefox에서만 접속 장애가 발생하더군요. 


본 페이지에서는 Firefox 웹브라우저를 이용하여 웹사이트에 접속시에 "SEC_ERROR_PKCS11_GENERAL_ERROR"라는 에러 메시지가 발생하면서 접속되지 않을 때 조치하는 방법에 대해서 설명하고자 합니다.


임시 조치 방법
---


해당 문제를 해결하기 위해서는 레지스트리 편집기를 실행시켜서 아래 레지스트리 값으로 수정하거나 추가하면 손쉽게 해결할 수 있습니다. 


### 1. 레지스트리 편집기 실행


가장 먼저 "윈도우 키" + "R" 키를 동시에 눌러서 "regedit"를 입력하여 레지스트리 편집기를 실행시킵니다.


### 2. HKEY_LOCAL_MACHINE 디렉토리를 선택합니다. 


최상위 경로에서 "HKEY_LOCAL_MACHINE" 항목을 선택합니다. 


### 3. SOFTWARE 디렉토리를 선택합니다. 


HKEY_LOCAL_MACHINE 디렉토리 하위에 있는 SOFTWARE 디렉토리를 선택합니다. 
HKEY_LOCAL_MACHINE\SOFTWARE


### 4. Policies 디렉토리를 선택합니다.


HKEY_LOCAL_MACHINE\SOFTWARE 디렉토리 하위에 있는 Policies 디렉토리를 선택합니다.
HKEY_LOCAL_MACHINE\SOFTWARE\Policies


### 5. Mozilla 디렉토리를 선택합니다. 


HKEY_LOCAL_MACHINE\SOFTWARE\Policies 디렉토리 하위에 있는 Mozilla 디렉토리를 선택합니다.
HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Mozilla


### 6. Firefox 디렉토리를 선택합니다. 


HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Mozilla 디렉토리 하위에 있는 Firefox 디렉토리를 선택합니다. 
HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Mozilla\Firefox


### 7. Preferences 디렉토리를 선택합니다. 없으면 생성합니다. 


HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Mozilla\Firefox 디렉토리 하위에 있는 Preferences 디렉토리를 선택합니다. 
만약 해당 키값이 없다면 마우스 오른쪽 버튼을 이용해서 "새로 만들기"를 선택하시고, "키(K)"를 눌러 "Preferences" 키를 생성합니다. 


### 8. security.osclientcerts.autoload 값을 0으로 변경합니다. 


HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Mozilla\Firefox\Preferences 디렉토리에서 "security.osclientcerts.autoload" 키를 선택해서 값을 0으로 변경합니다. 만약 해당 값이 없다면 "새로 만들기" 메뉴를 이용해서 "DWORD(32비트) 값"을 추가하고 값은 0으로 지정해줍니다. 


### 9. Firefox를 재시작합니다. 


그 후에 Firefox를 시작하면 해당 문제가 해결됩니다. 


관련 링크
---


해당 내용은 아래의 페이지에서 정보를 얻었습니다.


{% assign preview_image_url = "/assets/images/firefox/firefox.png" %}
{% assign preview_url = https://github.com/orange-cloudfoundry/paas-templates/issues/891 %}
{% assign preview_title = 'Expected behavior As a paas-templates operator and user In order to use portals and web ui components with Firefox browser I need to adapt web access to entreprise strategy Observed behavior Since ...' %}
{% assign preview_description = 'None' %}
{% include body-preview.html %}