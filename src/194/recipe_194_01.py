from datetime import datetime

# 문자열에서 datetime 타입을 생성
dt = datetime.strptime("2021/10/12 12:05:00", "%Y/%m/%d %H:%M:%S")

# datetime 타입에서 문자열로 변환
datetime_str = dt.strftime("%Y-%m-%d %H:%M:%S")
print(datetime_str)
