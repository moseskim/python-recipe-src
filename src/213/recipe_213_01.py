from urllib import parse

url = "https://docs.python.org/ko/3/search.html?q=%EB%B3%80%EC%88%98&check_keywords=yes&area=default"
p = parse.urlparse(url)
print(p)
print(p.scheme)
print(p.netloc)
print(p.path)
print(p.query)
