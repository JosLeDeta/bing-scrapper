from bing_utils import SimpleSearch, BingResult
from multiprocessing import Process
import json

terms = ['test', 'scrapping', 'test typefile: pdf inurl: *.pdf']

def ThreadSearch(term, n_pages=1):
    data = SimpleSearch(term, n_page=1)
    name = term.replace(' ', '-').replace(':', '').replace('*', '').replace('.','')
    with open(f'json_files/{name}.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, ensure_ascii=False))

if __name__ == '__main__':
    n_tasks = len(terms)
    for term in terms:
        Process(target=ThreadSearch, args=[term, ]).start()