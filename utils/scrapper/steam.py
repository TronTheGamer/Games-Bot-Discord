import requests
from bs4 import BeautifulSoup as BS
import json
import re


library = open('steam.json')
STEAM = json.load(library)
FREE_URL = STEAM['free_url']
# print(URL)
response = requests.get(FREE_URL)
soup = BS(response.text, 'lxml')
GAME_TAG = str(STEAM['div_class']['name'])
GENRE_TAG = str(STEAM['div_class']['genre'])
GENRE_ITEM_TAG = str(STEAM['span_class']["genre_item"])
# print(GAME_TAG)
regex_name = re.compile(rf"<div class=\"{GAME_TAG}\">\s*(.*)?\s*<")
GAMES_NAMES = [str(regex_name.match(str(x)).group(1)) for x in soup.findAll('div', attrs={'class': GAME_TAG})]
# print(GAMES_NAMES)

regex_genre_item = re.compile(rf"<span class=\"{GENRE_ITEM_TAG}\">\s*(.*)?\s*<")
GAMES_GENRE = [[str(y).replace(f"<span class=\"{GENRE_ITEM_TAG}\">","").replace(f"</span>","").strip() for y in re.findall(regex_genre_item, str(x))] for x in soup.findAll('div', attrs={'class': GENRE_TAG})]
# GAMES_GENRE.append(GAMES_GENRE[0])
# GAMES_GENRE = GAMES_GENRE[1:]
# # print(GAMES_GENRE)
FINAL_PRICE_TAG = str(STEAM['div_class']['final_price'])

FINAL_PRICE = [str(price).replace(f"<div class=\"{FINAL_PRICE_TAG}\">","").replace("</div>","").strip() for price in soup.findAll('div',attrs={'class':f'{FINAL_PRICE_TAG}'})]
print(FINAL_PRICE,len(FINAL_PRICE))
GAME_DICT = {}

# print(len(GAMES_GENRE))
# print(len(GAMES_NAMES))

for i in range(len(GAMES_GENRE)):
    GAME_DICT[GAMES_NAMES[i]] = {\
        'genre':GAMES_GENRE[i],\
        # 'price': FINAL_PRICE[i]\
        }

print(GAME_DICT)