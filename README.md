 
# KT_Internet_Reset_Python

## KT 인터넷 초기화를 자동으로 해주는 파이썬 스크립트입니다.

![Generic badge](https://img.shields.io/badge/Version-1.0.0-{color}.svg)  [![Generic badge](https://img.shields.io/badge/Docker-KT_Internet_Reset_Python-blue.svg)](https://hub.docker.com/r/rlatn1234/kt_internet_reset)

## 필요한 파일

 - [Chrome](https://www.google.com/chrome/) 
 - [설치된 크롬과 동일한 버젼의 ChromeDriver](https://chromedriver.chromium.org/downloads)

## 설치하기

1. OS와 맞는 ChromeDriver를 다운받아 KT_Reset.py 파일과 동일한 폴더에 붙여넣기 합니다.
    
2. Requirement 설치

```python
python3 -m pip install -r requirement.txt
```
3. 스크립트 실행

```python
python3 KT_Reset.py
```
## 자동화 도커 [Docker Hub](https://hub.docker.com/r/rlatn1234/kt_internet_reset)

- 우분투가 설치된 도커를 수정하여 하루에 한번씩 자동으로 초기화하도록 설정하였습니다.
- 테스트중이므로 버그가 있을수 있습니다.
