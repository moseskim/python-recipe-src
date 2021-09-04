import requests

url = "https://httpbin.org/get"
proxies = {"http": "http://xxx.xxx.xxx.xxx:3128", "https": "https://xxx.xxx.xxx.xxx:3128"}
requests.get(url, proxies=proxies)
# requests.get(url, timeout=(3, 30))
