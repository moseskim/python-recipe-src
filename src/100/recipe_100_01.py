import traceback

try:
    x = 1 / 0
except Exception as e:
    # 문자열을 얻는 format_exc() 메서드
    print("에러 정보\n" + traceback.format_exc())
