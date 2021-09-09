from datetime import datetime

# 현재 시각 얻기
dt = datetime.now()

# datetime 타입에서 문자열로 변환
datetime_str = dt.strftime("%Y-%m-%d %H:%M:%S")
print(datetime_str)
