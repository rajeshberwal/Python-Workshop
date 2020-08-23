import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')

quotes = soup.findAll('span', class_='text')
authors = soup.findAll('small', class_='author')
tags = soup.findAll('div', class_='tags')

for i in range(len(quotes)):
    print(quotes[i].text)
    print('Author: ', authors[i].text)
    quote_tags = tags[i].findAll('a', class_='tag')
    for tag in quote_tags:
        print(tag.text, end=' ')