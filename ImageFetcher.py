import requests
from bs4 import BeautifulSoup
import os
import urllib


class ImageFetcher:
    def __init__(self):
        self.GOOGLE_IMAGE = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

    def fetch_images(self, query: str, num_images: int):
        query = query.split()
        query = '+'.join(query)
        url = self.GOOGLE_IMAGE + 'q=' + query + '&oq=' + query
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.findAll('img', {'class': 'rg_i Q4LuWd'})

        # get 'num_images' number of images
        links = []
        for i, result in enumerate(results):
            try:
                link = result['data-src']
                links.append(link)
                if i == num_images - 1:
                    break
            except KeyError:
                continue

        return links