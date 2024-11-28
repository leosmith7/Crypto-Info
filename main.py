from bs4 import BeautifulSoup
import requests
import csv

URL = "https://finance.yahoo.com/markets/crypto/all/"



response = requests.get(url=URL).text

soup = BeautifulSoup(response, "html.parser")



symbols = [symbol.text.strip() for symbol in soup.find_all('span', class_='symbol', limit=25)]
#print(symbols)
dollar_changes = []
percentage_changes = []
market_caps = []
volumes = []
prices = []

for I in range(0, len(symbols)):
    print(symbols[I])
    prices.append(soup.find('fin-streamer', attrs={'data-field' : 'regularMarketPrice',  'data-symbol':{symbols[I]}}).text)
    dollar_changes.append(soup.find('fin-streamer', attrs={'data-field' : 'regularMarketChange',  'data-symbol':{symbols[I]}}).text)
    percentage_changes.append(soup.find('fin-streamer', attrs={'data-field' : 'regularMarketChangePercent',  'data-symbol':{symbols[I]}}).text)
    market_caps.append(soup.find('fin-streamer', attrs={'data-field' : 'marketCap',  'data-symbol':{symbols[I]}}).text)
    volumes.append(soup.find('fin-streamer', attrs={'data-field' : 'regularMarketVolume',  'data-symbol':{symbols[I]}}).text)


with open('crypto_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Symbol', 'Price', 'Dollar Change', 'Percentage Change', 'Market Cap', 'Volume'])

    for i in range(len(symbols)):
        writer.writerow([symbols[i], prices[i], dollar_changes[i], percentage_changes[i], market_caps[i], volumes[i]])






