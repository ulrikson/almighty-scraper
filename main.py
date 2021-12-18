from HtmlParser import HtmlParser
from KeywordGenerator import KeywordGenerator

url = "https://www.theguardian.com/world/2021/dec/18/scientists-watch-giant-doomsday-glacier-in-antarctica-with-concern"
headers = None
text = HtmlParser(url, headers).getAllText()

keywords = KeywordGenerator(text).generateWithSpacy()

print(keywords)