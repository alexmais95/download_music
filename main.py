from bs4 import BeautifulSoup
import requests
import json
import lxml
from setting import *
import json
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def make_html(url, header, name_file):
    req = requests.get(url, headers=header)
    site_text = req.text
    with open(f'{name_file}.html', 'w', encoding='utf-8') as f:
        file = f.write(site_text)
    return file


def link_for_downlod():
    with open('site_drive.html', encoding='utf-8') as f:
         site = f.read()

    soup = BeautifulSoup(site, 'lxml')

    find_el = soup.find_all(class_='popular-play-author')

    data = []
    for element in find_el:
        a_href = element.get('href')
        el = 'https://drivemusic.club' + a_href
        data.append(el)


    with open('music_linc1.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def download_music(file_name):
    with open(f'{file_name}.json', encoding='utf-8') as f:
        file = json.load(f)
    for el in file:
        browser = webdriver.Firefox()
        browser.maximize_window()
        browser.get(el)
        time.sleep(5)

        find = browser.find_element(By.XPATH, '//a[@class="song-author-btn btn-download"]')
        find.click()
