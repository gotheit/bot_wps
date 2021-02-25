from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import pickle

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome(r"C:\Users\diego\PycharmProjects\bot_wps\driver\chromedriver.exe",options=chrome_options)

#driver.get("https://web.whatsapp.com/")
#time.sleep(10)

celular = "NUMERO DE TELEFONO"
mensaje = ["Hola soy un bot de mensajeria, basicamente un robot. A continuacion, llegaran una serie de mesanjes de prueba.","Primer mensaje de prueba :)","Hola llego el mensaje?(●'◡'●)","Creo que no ha llegado el mensaje, alo!!","Esta seguro que usted no es una maquina como yo? (●'◡'(╯°□°）╯︵ ┻━┻●)"
           ,"jejejejjejejejejjejejeje."]
print("---bot mensaje wps---")
print("Numero: "+ celular)
for mns in mensaje:
    print("Mensaje: "+mns)
    driver.get("https://wa.me/" + celular + "?text=" + mns)
    time.sleep(3)
    # paso 1
    btn = driver.find_elements_by_xpath("//*[@id='action-button']")[0]
    btn.click()
    time.sleep(3)
    # paso 2
    btn = driver.find_elements_by_xpath("//*[@id='fallback_block']/div/div/a")[0]
    btn.click()
    time.sleep(15)
    # paso 3
    btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")[0]
    btn.click()
    time.sleep(1)

time.sleep(5)
driver.close()
