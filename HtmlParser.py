from bs4 import BeautifulSoup


class HtmlParser:
    def __init__(self, html):
        self.html = html

    def extract(self):
        file = open(self.html)
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        return soup

        # find top level tag --> create "level"
        # All its children --> new "levels"
        # All their childrem --> levels of that level
