import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/detail_basic/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

result = soup.findAll('div', class_='card mt-4 my-4')

for elem in result:
  if elem.find('img'):
    print(elem.find('img')['src'])
  print(elem.text)