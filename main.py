from HtmlParser import HtmlParser

# For testing purposes
html = "test.html"

test = HtmlParser(html).extract()
print(test)
