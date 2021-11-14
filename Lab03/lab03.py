import json
from rich.console import Console
import rich.traceback
import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description = "Arguments description")
parser.add_argument('-url', '--u1', help = 'page url', default = 'https://www.filmweb.pl/ranking/serial')
parser.add_argument('-file', '--j1', help = 'json file', default = 'lab03.json')
args = parser.parse_args()

console = Console()
console.clear()
rich.traceback.install()


req = requests.get(args.u1)
soup = BeautifulSoup(req.text, 'html.parser')
divs = soup.find_all('div', class_ = 'rankingType')
i = 0
x = []
for div in divs:
    i = i + 1
    x.append(f"Miejsce w rankingu: {i}, Data wydania: {div.find('span', class_ = 'rankingType__year')['content']}, Link: {'https://www.filmweb.pl'}{div.find('a')['href']}")

with open(args.j1, 'w') as f:
    json.dump(x, f)







