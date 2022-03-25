from bs4 import BeautifulSoup
import requests

class BingResult:
    def __init__(self, html):
        self.title = html.find('h2').text
        self.link = html.find('h2').find('a').get('href')
        self.desc = html.find('p').text if html.find('p') else None

    def toJson(self):
        return {'title': self.title, 'link': self.link, 'desc': self.desc}

def DownloadPage(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
    data = requests.get(url, headers=headers)
    return BeautifulSoup(data.text, 'lxml')

def SimpleSearch(word, n_page=1):
    n_page = n_page if n_page == 1 else (n_page - 1) * 11
    page = DownloadPage('https://www.bing.com/search?q={}&form=QBLH&sp=-1&sc=8-4&qs=n&sk=&cvid=A8EDA7D634454F678E5E3444584CC3CA&first={}'.format(word, n_page))
    data = [ BingResult(li).toJson() for li in page.select('li.b_algo')]
    return data