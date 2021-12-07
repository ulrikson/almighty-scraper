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

    def getJsonResponse(self):
        response = self.get()
        json = response.json()
        return json

    def getAutoResponse(self):
        try:
            return self.getJsonResponse()
        except JSONDecodeError:
            return self.getTextResponse()
