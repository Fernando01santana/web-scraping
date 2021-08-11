import time
import requests
import pandas as pd
import html5lib
import xmltojson
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import json

# 1. Pegar conteudo
url = "https://play.google.com/store"

option = Options()
option.headless = True
# driver = webdriver.Chrome(options=option)
driver = webdriver.Chrome(
    executable_path='C:/Users/coolf/AppData/Local/chromedriver.exe')
driver.get(url)
time.sleep(5)

driver.find_element(By.NAME, "q").send_keys("COD")
driver.find_element(By.ID, 'gbqfb').click()
time.sleep(2)

driver.find_element_by_link_text(
    'Call of Duty®: Mobile - 6ª TEMPORADA: ESQUENTOU').click()
time.sleep(3)

element = driver.find_element(By.CLASS_NAME, "W4P4ne")
html_content = element.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')
print(soup)
comment = soup.find_all('div', "UD7Dzf")


# comment = soup.find(jsname="bN97Pc")

driver.quit()

with open("data.html", "w") as html_file:
    html_file.write("<meta charset='utf-8'>" + str(comment))

with open("data.html", "r") as html_file:
    html = html_file.read()
    html = html.replace("[", "")
    html = html.replace("]", "")
    html = html.replace("\ ", "")
    json_ = xmltojson.parse(html)


for i in range(0, len(json_)):
    json_ = json_.replace("\ ", "")


with open('data.json', 'w', encoding='utf-8') as jp:
    js = json.dumps(json_, indent=4)
    jp.write(js)
