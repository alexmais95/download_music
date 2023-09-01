from bs4 import BeautifulSoup
import requests
import json
import lxml

url = 'https://drivemusic.club/novinki_muzyki'
header = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
req = requests.get(url, headers=header)

site_text = req.text

with open('site_drive.html', 'w', encoding='utf-8') as f:
     file = f.write(site_text)


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

link_for_downlod()
