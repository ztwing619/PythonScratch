from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import smtplib
from email.mime.text import MIMEText

# 設置Chrome選項
chrome_options = Options()
chrome_options.add_argument("load-extension=C:\\instant_data_scraper")  # 更新為解壓縮後的文件夾路徑

# 啟動Chrome瀏覽器
service = Service(r'Z:\chromedriver-win64\chromedriver-win64\chromedriver.exe')  # 確保這裡是 chromedriver.exe 的完整路徑
driver = webdriver.Chrome(service=service, options=chrome_options)

def fetch_hot_posts():
    driver.get('https://www.dcard.tw/f')
    time.sleep(10)  # 等待頁面加載和擴展運行
    # 這裡可以模擬點擊 Instant Data Scraper 圖標，具體取決於擴展的設計
    time.sleep(30)  # 等待數據抓取完成
    # 導出數據（需要手動操作或使用Selenium點擊導出按鈕）
    # 保存為 Excel 或 CSV 文件
    # 示例：
    # driver.find_element_by_xpath('//button[text()="Export"]').click()
    # 暫時返回空數據列表
    return []

def check_heat(data):
    threshold_likes = 100
    threshold_comments = 50
    for post in data:
        if post['likes'] > threshold_likes or post['comments'] > threshold_comments:
            return True
    return False

# 設定熱度閾值
threshold_likes = 100
threshold_comments = 50

# 初始抓取頻率
fetch_interval = 3  # 每三秒抓取一次

while True:
    data = fetch_hot_posts()
    if check_heat(data):
        fetch_interval = 3  # 每三秒抓取一次
    else:
        fetch_interval = 3  # 每三秒抓取一次
    time.sleep(fetch_interval)
