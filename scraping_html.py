import requests_html
from requests_html import HTMLSession

session = HTMLSession() #宣告HTMLSession
r = session.get('https://www.google.com.tw/?hl=zh_TW') #get請求
r = session.post('https://www.google.com.tw/?hl=zh_TW',data = {})  #post請求

#資料清洗 把顯而易見的錯誤處理掉。
print(r.html.url)#印出網頁網址
print(r.html.links)#印出網頁內容的所有網址
print(r.text)#印出網頁內容（HTML）
print(r.html.text)#印出網頁文字內容

# Requests-HTML被廣泛使用是他支援多種不一樣的功能。

#JavaScript
#CSS選擇器
#Xpath選擇器
#自定義模擬User-Agent
#自動追蹤定向
#Cookie持久化
#非同步請求

#資料定位

#find()
    # selector：CSS選擇器。
    # containing：傳入字串，使定位的元素包含此字串，預設為None。
    # clean：是否清除、忽略HTML的標籤，預設為False。
    # first：是否指尋找到第一個定位到的元素，預設為False。
    # _encoding：編碼格式，預設為None。
#xpath()
    # selector：Xpath選擇器。
    # clean：是否清除、忽略HTML的標籤，預設為False。
    # first：是否指尋找到第一個定位到的元素，預設為False。
    # _encoding：編碼格式，預設為None。
#search()
    # template：傳回第一個符合template的字串{}部分。
#search_all()
    # template：傳回符合template的字串{}部分。