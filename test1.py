from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import smtplib
from email.mime.text import MIMEText

proxy = "35.185.196.38:3128"
chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy}')
chrome_options.add_extension("load-extension=C:\\instant_data_scraper")

# 启动Chrome浏览器
service = Service(r'Z:\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

def fetch_hot_posts():
    driver.get('https://www.dcard.tw/f')
    time.sleep(10)
    # 模拟点击Instant Data Scraper图标
    time.sleep(30)  # 等待数据抓取完成
    return []

def check_heat(data):
    threshold_likes = 100
    threshold_comments = 50
    for post in data:
        if post['likes'] > threshold_likes or post['comments'] > threshold_comments:
            return True
    return False

fetch_interval = 3600
while True:
    data = fetch_hot_posts()
    if check_heat(data):
        fetch_interval = 600
    else:
        fetch_interval = 3600
    time.sleep(fetch_interval)
