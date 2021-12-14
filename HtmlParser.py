from bs4 import BeautifulSoup
from Scraper import Scraper
import re


class HtmlParser:
    def __init__(self, url, headers):
        Scraper.__init__(self, url, headers)

    def extractHtml(self):
        content = Scraper.getContent(self)
        cleanHtml = BeautifulSoup(content, "html.parser")
        return cleanHtml
    
    def getAllText(self):
        html = self.extractHtml()
        text = re.sub("[\t\n]", " ", html.text)
        return text
    
    def test(self):
        return self.getAllText()
