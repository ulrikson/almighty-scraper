from json.decoder import JSONDecodeError
import requests


class Scraper:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get(self):
        response = requests.get(self.url, self.headers)
        return response

    def getTextResponse(self):
        response = self.get()
        text = response.text
        return text
