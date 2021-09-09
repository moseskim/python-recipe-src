from datetime import date, datetime

# 문자열에서 datetime 타입을 생성한 뒤, date 타입으로 변환
d = datetime.strptime("2021/10/12", "%Y/%m/%d").date()

# date 타입에서 문자열로 변환
date_str = d.strftime("%Y-%m-%d")
print(date_str)
