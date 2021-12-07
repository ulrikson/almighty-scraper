from Scraper import Scraper


class HtmlParser(Scraper):
    def __init__(self, url, headers):
        Scraper.__init__(self, url, headers)

    def clean(self):
        html = Scraper.getTextResponse(self)
        return html
