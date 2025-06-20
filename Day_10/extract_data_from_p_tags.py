from bs4 import BeautifulSoup
import requests
import json
import os

path = os.path.abspath(__file__)[::-1].partition('\\')[-1][::-1] + '\\'

URL = "https://www.niet.co.in/"

res = requests.request('GET', URL)

if res.status_code != 200:
    print("Could not fetch the website contents\nStatus Code: ", res.status_code)
else:
    print("Sucess\nStatus Code: ", res.status_code, end="\n\n")

data = res.content

soup = BeautifulSoup(data, 'lxml')

paragraphs = soup.find_all('a')

for i, a in enumerate(paragraphs):
    try:
        print(f"{i} - {a['href']}")
    except: pass