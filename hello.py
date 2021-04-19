import requests
import json
from bs4 import BeautifulSoup as Bs

base_url = 'https://ru-ru.soccerwiki.org/'
extra_url = 'league.php?leagueid=28'

html = requests.get('https://www.udemy.com/api-2.0/discovery-units/all_courses/?p=1&page_size=16&subcategory=&instructional_level=&lang=ru&price=&duration=&closed_captions=&subs_filter_type=&category_id=288&source_page=category_page&locale=ru_RU&currency=rub&navigation_locale=en_US&skip_price=true&sos=pc&fl=cat')
html2 = html.json()
print(html2)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(html2, f, ensure_ascii=False, indent=4)