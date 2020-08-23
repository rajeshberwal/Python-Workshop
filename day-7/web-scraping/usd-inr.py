import requests
from bs4 import BeautifulSoup
from time import sleep

url = 'https://in.finance.yahoo.com/quote/INR=X?p=INR=X'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

price = soup.find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')

while True:
    print(f'1USD: {price.text}INR')
    sleep(5)