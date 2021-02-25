from selenium import webdriver
import time
import os
import pickle

driver = webdriver.Chrome(executable_path=r"C:\Users\diego\PycharmProjects\bot_wps\driver\chromedriver.exe")
driver.get("https://web.whatsapp.com/")

time.sleep(10)
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))


