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
import io
import gzip

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
buttons = driver.find_elements_by_class_name('OzU4dc')

time.sleep(2)

driver.find_element_by_link_text(
    'Call of Duty®: Mobile - 6ª TEMPORADA: ESQUENTOU').click()
time.sleep(3)

elements = driver.find_elements_by_class_name("UD7Dzf")
elements.find
cont = len(elements)
html_content = []
for element in range(0, cont):
    html_content.append(elements[element].get_attribute('outerHTML'))

cont2 = len(html_content)
soup = []
for content in range(0, cont2):
    soup.append(BeautifulSoup(
        html_content[content], 'html.parser'))


driver.quit()

# with open("data.html", "w") as html_file:
#     html_file.write(str(soup))

with open("data.html", "r") as html_file:
    html = io.BytesIO(soup[0].root)
    coded = gzip.GzipFile(fileobj=html)
    decoded = coded.read()
    content = decoded.decode("utf-8")
    # html = html.replace("[", "")
    # html = html.replace("]", "")
    # html = html.replace(",", "")
    json_ = xmltojson.parse(content)

print(content)
with open('data.json', 'w', encoding='utf-8') as jp:
    js = json.dumps(json_, indent=4)
    jp.write(js)
