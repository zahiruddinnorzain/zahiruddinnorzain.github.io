# pip3 install beautifulsoup4
# pip3 install lxml

from bs4 import BeautifulSoup
import requests
import os

def news():
    print('---------------------------------')
    print('--------------NEWS---------------')
    print('---------------------------------')
    url = 'https://markets.businessinsider.com/news'
    baseurl = 'https://markets.businessinsider.com'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    tableisi = soup.find_all('a', class_='image-news-list__link')

    print(tableisi[0].text)

    for data in tableisi:
        print(data.text.lstrip())
        print(baseurl+data['href'])
        print('------------------------------------------\n\n\n\n\n')

#------------------------------------------------------------------------
def news2():
    print('-----------------------------------')
    print('--------------NEWS 2---------------')
    print('-----------------------------------')

    url = 'https://markets.businessinsider.com/news'
    baseurl = 'https://markets.businessinsider.com'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    tableisi = soup.find_all('a', class_='latest-news__link')

    # print(tableisi[0].text)
    # print(soup)

    for data in tableisi:
        print(data.text.lstrip())
        print(baseurl+data['href'])
        print('------------------------------------------\n\n\n\n\n')

#------------------------------------------------------------------------
def commodities():
    print('----------------------------------------')
    print('--------------COMMODITIES---------------')
    print('----------------------------------------')
    url = 'https://markets.businessinsider.com/commodities'
    baseurl = 'https://markets.businessinsider.com'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    tableisi = soup.find_all('a', class_='popular-articles__link')

    # print(tableisi[0].text)
    # print(soup)

    for data in tableisi:
        print(data.text.lstrip())
        print(baseurl+data['href'])
        print('------------------------------------------\n\n\n\n\n')

#------------------------------------------------------------------------
def etfs():
    print('----------------------------------------')
    print('--------------ETF---------------')
    print('----------------------------------------')
    url = 'https://markets.businessinsider.com/etfs'
    baseurl = 'https://markets.businessinsider.com'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    tableisi = soup.find_all('a', class_='popular-articles__link')

    # print(tableisi[0].text)
    # print(soup)

    for data in tableisi:
        print(data.text.lstrip())
        print(baseurl+data['href'])
        print('------------------------------------------\n\n\n\n\n')

#------------------------------------------------------------------------
def stocks():
    print('----------------------------------------')
    print('--------------STOCKS---------------')
    print('----------------------------------------')
    url = 'https://markets.businessinsider.com/stocks'
    baseurl = 'https://markets.businessinsider.com'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    tableisi = soup.find_all('a', class_='popular-articles__link')

    # print(tableisi[0].text)
    # print(soup)

    for data in tableisi:
        print(data.text.lstrip())
        print(baseurl+data['href'])
        print('------------------------------------------\n\n\n\n\n')

#------------------------------------------------------------------------
def indices():
    print('----------------------------------------')
    print('--------------INDICES---------------')
    print('----------------------------------------')
    url = 'https://markets.businessinsider.com/indices'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    tableisi = soup.find_all('a', class_='popular-articles__link')

    # print(tableisi[0].text)
    # print(soup)

    for data in tableisi:
        print(data.text.lstrip())
        print(url+data['href'])
        print('------------------------------------------\n\n\n\n\n')

#------------------------------------------------------------------------
def crypto():
    print('----------------------------------------')
    print('--------------CRYPTO---------------')
    print('----------------------------------------')
    url = 'https://markets.businessinsider.com/cryptocurrencies'
    baseurl = 'https://markets.businessinsider.com'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    tableisi = soup.find_all('a', class_='popular-articles__link')

    # print(tableisi[0].text)
    # print(soup)

    for data in tableisi:
        print(data.text.lstrip())
        print(baseurl+data['href'])
        print('------------------------------------------\n\n\n\n\n')

def main():
    print('1 : NEWS\n')
    print('2 : NEWS 2\n')
    print('3 : COMMODITIES\n')
    print('4 : ETF\n')
    print('5 : STOCKS\n')
    print('6 : INDICES\n')
    print('7 : CRYPTO\n')
    ans = input('Watch news = ')
    os.system('clear')

    if ans == '1':
        news()
    elif ans == '2':
        news2()
    elif ans == '3':
        commodities()
    elif ans == '4':
        etfs()
    elif ans == '5':
        stocks()
    elif ans == '6':
        indices()
    elif ans == '7':
        crypto()
    elif ans == '99':
        exit(1)
    else:
        print("==NONE==")

    main()

main()

