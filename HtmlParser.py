from bs4 import BeautifulSoup
from Scraper import Scraper


class HtmlParser:
    def __init__(self, url, headers):
        Scraper.__init__(self, url, headers)

    def extractHtml(self):
        content = Scraper.getContent(self)
        cleanHtml = BeautifulSoup(content, "html.parser")
        return cleanHtml

    def getTextRelatedTags(self):
        headerTags = [f"h{x}" for x in range(1, 7)]
        otherTextTags = ["p"]
        allTags = headerTags + otherTextTags
        return allTags

    def getAllText(self):
        html = self.extractHtml()
        textTags = html.find_all(self.getTextRelatedTags())
        text = [tag.text for tag in textTags]
        return " ".join(text)
