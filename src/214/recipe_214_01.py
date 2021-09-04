from urllib import parse

url = "q=%EB%B3%80%EC%88%98&check_keywords=yes&area=default"
q = parse.parse_qs(url)
print(q)
