import requests
from bs4 import BeautifulSoup


class WebSearcher:
    def __init__(self):
        self.GOOGLE_SEARCH = 'https://www.google.com/search?q='

    def search(self, query: str):
        url = self.GOOGLE_SEARCH + query.replace(' ', '+')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.select('.kCrYT a')

        links = []
        for result in search_results:
            link = result.get('href')
            if link.startswith('/url?q='):
                link = link[7:]
                links.append(link)

        return links