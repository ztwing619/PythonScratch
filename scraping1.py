import requests

#  ?後面攜帶參數   多個參數用&連接
url = 'https://www.google.com.tw/?hl=zh_TW'
r = requests.get(url)
print(type(url),r) #response 200 網頁正常

# auth指定帳號、密碼
# r1 = requests.get('url', auth = ('user', 'pass'))

# post 向指定資源提交請求
mydata = {
    'key':'value'
}

try :
    r = requests.post('url',data=mydata)
    r.raise_for_status()  # 檢查請求是否成功（狀態碼在2xx範圍內）
    print(r.json()) # 假設伺服器返回JSON數據
except :
    print('發生錯誤')
    
myfile = {'myfile':open('myfile.docx','rb')}#要上傳的檔案
r = requests.post('url',file = myfile) #requests.post並指定files參數