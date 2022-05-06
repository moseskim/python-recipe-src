# 제이펍 도서 정보의 URL 또는 html 구조가 달라지는 경우 이 코드는 정상 동작하지 않습니다.
# 그때는 변수 html 데이터를 디렉터리에 포함된 jpub.html로 바꾸기 바랍니다.
# 다음은 html 데이터 치환의 예입니다.
# with open("jpub.html", "r", encoding="utf-8") as f:
#     html = f.read()

import requests
from bs4 import BeautifulSoup

# 도서 정보 URL
url = "https://jpub.tistory.com/category/%EB%8F%84%EC%84%9C%20%EC%86%8C%EA%B0%9C"

# HTTP GET 요청
r = requests.get(url)

# html 얻기
html = r.text

# html 파싱
soup = BeautifulSoup(html, "html5lib")

# post-item 태그 얻기
post_items = soup.find_all(name="div", class_="post-item")

# post-item 태그별로 서적 정보 얻기
for post_item in post_items:
    link_text = post_item.find(class_="title").getText()
    link = post_item.find("a")
    print(link_text, link.get("href"))
