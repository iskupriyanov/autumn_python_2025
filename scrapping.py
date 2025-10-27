import requests
from bs4 import BeautifulSoup
import json

url = 'https://python-academy.org/ru/guide/oop'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
# paragraphs = soup.find_all('strong')
elements = soup.select('ol>li')

for row in elements:
    print (row.text.split('—'))
json.dump
