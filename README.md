# Hotlimy(Hot Deal Alimy) v1.1

직접 쓰려고 만든 텔레그램 핫딜 알리미

타겟리스트에 타겟을 추가하면,

주기적으로 해당 타겟이 핫딜게시판에 올라와있는지 체크하여 봇이 메세지를 보냄

## 지원 사이트

- [FMKOREA 핫딜](https://www.fmkorea.com/hotdeal)
- [PPOMPPU 핫딜](https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu)

## 설치 및 실행
### Python3

```python
# *************************************
#
# .env 파일 생성 후 아래 두 줄 저장
#
# TOKEN = "{BOT_TOKEN}"
# CHAT_ID = "{CHAT_ID}"
#
# BOT_TOKEN, CHAT_ID 생성법은 구글 참고
# *************************************


# 가상환경 생성 및 실행
python -m venv venv
source venv/bin/activate

# 라이브러리 설치
pip install requirements.txt

# Hotlimy 실행
python main.py
```

## 명령어

- `/help`: 도움말
- `/add target1 target2 ...`: 타겟리스트에 타겟 추가
- `/del target1 target2 ...`: 타겟리스트에서 타겟 삭제
- `/targets`: 현재 타겟리스트 보기

## Release

### v1.1

- PPOMPPU 핫딜 지원
- Console log 지원

### v1.0

- Initial version

## Contact

email: harveydev24@gmail.com
