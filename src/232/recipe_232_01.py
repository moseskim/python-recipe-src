import requests

r = requests.get("https://httpbin.org/get")

# 인코딩
print(r.encoding)

# http 상태 코드
print(r.status_code)

# 응답 헤더
print(r.headers)
