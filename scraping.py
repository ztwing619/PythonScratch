import requests
#get 向指定資源提交請求，可以設定params參數字典。
#post 向指定資源提交請求，可以設定data參數字典。
#put 向指定資源提供最新內容，可以設定data參數字典。
r = requests.put('url', data = {'key':'value'})

# 請求 "刪除" 指定資源
r = requests.delete('url')
# 請求伺服器提供可用的功能"選項"
r = requests.options('url')
print(r.text) #回應訊息str(字串)

print(r.encoding) #回應、指定訊息編碼

print(r.url) #回應資源的URL地址

print(r.stutus_code) #回應狀態(int)

print(r.header) #回應訊息的標題(dict)

print(r.cookie) #回應訊息的cookie(dict)

print(r.history) #請求歷史(list)

#取得的資料是JSON格式，用".josn()"將訊息解碼後回傳(dict)。
r = requests.get('url')
r.josn()

#有時候網站會擋掉python-request的請求，因此會需要自訂Header。
#變數名字中間只能用"-"分隔，非標準協定頭欄位需要加上"x-"作為標示。
url = 'URL地址'
headers = {'變數':'變數'}
r = r.request(url, headers = headers)

#Timeout:檢查是否可以存取，或是避免在維修中或是故障的網站停留。
requests.get('url',timeout = [SECOND]) #以「秒」為單位。

#取得及修改Cookie
#取得
url = 'URL'
r = requests.get(url)
r.cookie['example_cookie_name'] 

#修改
url = 'URL'
cookie = dict(cookie_are = '')
r = request.get(url, cookie = cookie)
r.text