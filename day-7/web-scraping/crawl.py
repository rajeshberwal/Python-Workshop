import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')

items = soup.findAll('div', class_='col-lg-4 col-md-6 mb-4')
count = 1

for item in items:
    item_name = item.find('h4', class_='card-title').text.split('\n')[1]
    item_price = item.find('h5').text
    print(f'{count}) Name: {item_name}, Price: {item_price}$')
    count += 1