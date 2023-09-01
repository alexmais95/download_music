from bs4 import BeautifulSoup
import requests
import lxml
from setting import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Make_Download:
    def __init__(self, url, header):
        self.url = url
        self.header = header

    def download(self, url, header):
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

    def create_download(self):
        for site in self.url:
            self.download(site, self.header)


# download = Make_Download(url, header)
# download.create_download()
