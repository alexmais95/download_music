from bs4 import BeautifulSoup
import requests
import lxml
from setting import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def make_html(url, header, name_file):
    req = requests.get(url, headers=header)
    site_text = req.text
    with open(f'{name_file}.html', 'w', encoding='utf-8') as f:
        file = f.write(site_text)
    return file


def downlod(url, header):
    req = requests.get(url, headers=header)
    site_text = req.text
    soup = BeautifulSoup(site_text, 'lxml')
    find_el = soup.find_all(class_='popular-play-author')

    for element in find_el:
        a_href = element.get('href')
        el = 'https://drivemusic.club' + a_href
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(el)
        find = browser.find_element(By.CLASS_NAME, 'add_word')
        find.click()
        time.sleep(5)


for site in url:
    downlod(site, header)




