from HtmlParser import HtmlParser

# Idea being that we only need to supply the url and maybe some headers to scrape any open website or JSON

# For testing purposes
url = "https://dn.se/om/klimatet"
headers = None
html = HtmlParser(url, headers)

print(html.clean())
