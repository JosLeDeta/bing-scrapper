from bing_utils import SimpleSearch
from multiprocessing import Process
import json

terms = ['scrapping', 'test typefile: pdf inurl: *.pdf', 'enthec']

def ThreadSearch(term, n_pages=1):
    print(f'[i] Scrapping term {term} with total pages: {n_pages}')
    data = []
    for n in range(n_pages):
        data.extend(SimpleSearch(term, n_page=n + 1))
    name = term.replace(' ', '-').replace(':', '').replace('*', '').replace('.','')
    with open(f'json_files/{name}.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, ensure_ascii=False))

if __name__ == '__main__':
    for term in terms:
        Process(target=ThreadSearch, args=[term, 5]).start()