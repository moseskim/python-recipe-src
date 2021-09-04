# 기술평론하의 신간 정보의 URL 또는 html 구조가 달라지는 경우, 다음 코드는 정상 동작하지 않습니다.
# 그 때는 변수 html 데이터를 디렉터리에 포함된 gihyo.html로 바꾸기 바랍니다.
# 다음은 html 데이터 치환의 예입니다.
# with open("gihyo.html", "r") as f:
#     html = f.read()

import requests
from bs4 import BeautifulSoup

# 신간 URL
url = "https://gihyo.jp/book/list"

# HTTP GET 요청
r = requests.get(url)

# html 얻기
html = r.text

# html 파싱
soup = BeautifulSoup(html, "html5lib")

# ul 태그 얻기
ul = soup.find("ul", class_="magazineList01 bookList01")

# ul 태그 아래의 li 태그를 시퀀스로 얻기
lis = ul.find_all("li")

# li 태그별로 서정 정보 얻기
for li in lis:
    link = li.find("h3").find("a")
    print(link.text, link.get("href"))
