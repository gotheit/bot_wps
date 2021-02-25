from selenium import webdriver
import time
import os


#options = webdriver.ChromeOptions()
#options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
#chrome_driver_path = r"C:\Users\diego\PycharmProjects\bot_wps\driver\chromedriver.exe"
#driver = webdriver.Chrome(chrome_driver_path)

driver = webdriver.Chrome(executable_path=r"C:\Users\diego\PycharmProjects\bot_wps\driver\chromedriver.exe")


driver.get("http://www.python.org")
time.sleep(10)
driver.close()
