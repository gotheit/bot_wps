
import time
import os
import pickle



from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome(r"C:\Users\diego\PycharmProjects\bot_wps\driver\chromedriver.exe",options=chrome_options)
driver.get('https://web.whatsapp.com')  # Already authenticated
time.sleep(30)