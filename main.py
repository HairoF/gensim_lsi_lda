import requests
import re
from bs4 import BeautifulSoup as Bs
print(re.match(r'\d', 'question_price_elm.text 1 2123'))


# url = 'https://www.udemy.com/courses/development/?p=1'
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36', 'accept-language': 'ru-RU,ru;q=0.9'}
# html = requests.get(url, headers=headers).text
# soup = Bs(html, 'html.parser')
# div = soup.find_all('div', class_="course-list--container--3zXPS")
