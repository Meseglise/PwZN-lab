import json
from rich.console import Console
import rich.traceback
import requests
from bs4 import BeautifulSoup
import argparse

console = Console()
console.clear()
rich.traceback.install()

req = requests.get('https://pitchfork.com/features/lists-and-guides/peoples-list-25th-anniversary/')
# console.print(req.status_code)
# console.print(req.headers)
# console.print(req.request.headers)
# console.print(req.text)

soup = BeautifulSoup(req.text, 'html.parser')
divs = soup.find_all('div', class_ = 'filmo-row')
divs_film_cathegory = soup.find('div', class_ = 'filmo-category-section')
divs_films = divs_film_cathegory.find_all('div', class_ = 'filmo-row')

for div in divs_films:
    console.print(f"{div.find('span').text.strip()} {div.find('a').text.strip()} =  https://www.imdb.com/name/nm0001569{div.find('a')['href']}")