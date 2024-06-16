import requests

url = 'https://www.google.com.tw/?hl=zh_TW'
r = requests.get(url)
print(r.text)