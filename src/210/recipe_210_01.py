from urllib import parse

text = "제이펍"
url_encoded = parse.quote(text)
print(url_encoded)
