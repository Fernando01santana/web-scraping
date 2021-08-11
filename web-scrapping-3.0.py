import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui
import json
import xmltojson
from selenium.webdriver.common.by import By
import time


utl_base = 'https://play.google.com/store/search?q=COD'
driver = webdriver.Chrome(
    executable_path='C:/Users/coolf/AppData/Local/chromedriver.exe')
driver.get(utl_base)

time.sleep(2)
apps = driver.find_elements_by_class_name('Ktdaqe')
driver.find_element_by_class_name('nnK0zc').click()
time.sleep(2)

comments = driver.find_elements_by_class_name('UD7Dzf')
site = []

cont = len(comments)
for c in range(0, cont):
    site.append(
        str({f'comment {c}': BeautifulSoup(comments[c].text, 'html.parser')}))

print(site[0])
driver.quit()
with open('data.json', 'w', encoding='utf-8') as jp:
    js = json.dumps(site[0], indent=4)
    jp.write(js)
