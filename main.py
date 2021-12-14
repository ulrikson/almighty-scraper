from HtmlParser import HtmlParser

url = "https://www.dn.se/sverige/tegmark-wisell-om-nya-atgarder-inga-overraskningar-infor-jul/"
headers = None
html = HtmlParser(url, headers)

print(html.test())