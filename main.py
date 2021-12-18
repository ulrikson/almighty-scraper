from HtmlParser import HtmlParser

url = "https://www.theguardian.com/world/2021/dec/18/scientists-watch-giant-doomsday-glacier-in-antarctica-with-concern"
headers = None
html = HtmlParser(url, headers)

print(html.test())