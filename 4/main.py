import requests
import csv
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)

def write_csv(data):
    with open('yaca.csv', 'a') as f:
        writer = csv.writer(f)
        pass

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find_all('li', class_='yaca-snippet')

    for li in lis:
        try:
            name = li.find('h2').text
        except:
            name = ''
    print(len(lis))


def main():
    url = 'https://yandex.ru/yaca/cat/Entertainment'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
