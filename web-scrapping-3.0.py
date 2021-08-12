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
# apps = driver.find_elements_by_class_name('Ktdaqe')
driver.find_element_by_class_name('nnK0zc').click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, 'XnFhVd').click()
time.sleep(3)

comments = driver.find_elements_by_class_name('UD7Dzf')
site = []

cont = len(comments)
for c in range(0, cont):
    commentVerify = str(BeautifulSoup(comments[c].text, 'html.parser'))
    if commentVerify != "":
        item = u" "+str(BeautifulSoup(comments[c].text, 'html.parser'))
        decoded = item.encode(
            'ascii', 'ignore').decode('ascii')
        site.append({f"comentario-{c}": decoded})

driver.quit()
contComments = len(site)
with open('data.json', 'w', encoding='utf-8') as jp:
    for count in range(0, contComments):
        jp.write(json.dumps(site[count], indent=4))
