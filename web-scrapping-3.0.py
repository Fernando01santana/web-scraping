import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui
import json
import xmltojson
from selenium.webdriver.common.by import By
import time
import pandas as pd


with open('apps.json', 'r') as json_file:
    apps = json.load(json_file)

contApp = len(apps)
for a in range(0, contApp):
    utl_base = 'https://play.google.com/store/search?q='+apps[a]
    driver = webdriver.Edge(
        executable_path='C:/Users/coolf/AppData/Local/edge/msedgedriver.exe')
    driver.get(utl_base)

    time.sleep(2)
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
            item = BeautifulSoup(comments[c].text, 'html.parser')
            site.append([apps[a], str(item)])

    siteDatFrame = pd.DataFrame(
        site, columns=['Search_term ', 'Comment'])

    driver.quit()
    siteDatFrame.to_excel('comments-'+apps[a]+'.xlsx', index='false')
