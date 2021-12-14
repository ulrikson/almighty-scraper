from HtmlParser import HtmlParser

url = "https://dn.se/om/klimatet"
headers = None
html = HtmlParser(url, headers)

print(html.getAllText())