---
title: 빌드 디렉토리 파일 설명
description: 
---


빌드 디렉토리 파일 설명
===


./auto.sh
---


crontab에 의해서 자동으로 실행되는 스크립트이다.
- git pull을 통해서 최신 소스를 가져온다.
- md 파일을 체크한다. (check_md_files.py)
- 사이트 맵을 작성한다. (make_site_map.py)
- 변경점이 있으면 리모트에 업데이트 하고 메일을 전송한다. 
- 모든 변경점을 리모트에 업데이트 한다.
