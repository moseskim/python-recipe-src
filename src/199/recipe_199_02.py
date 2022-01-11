from datetime import datetime, date, time, timedelta

# 2021/12/22의date 타입 생성
d1 = date(2021, 12, 22)

# 2021/12/22 12:00:30의 datetime 타입 생성
dt1 = datetime(2021, 12, 22, 12, 00, 30)

# 100일 만큼의 timedelta 타입 생성
delta = timedelta(days=100)

# 100일 전의 날짜 및 시간 계산
d2 = d1 - delta
dt2 = dt1 - delta

# 계산 결과 출력
print(d2)
print(dt2)
