from bs4 import BeautifulSoup
from Scraper import Scraper
import yake
from rake_nltk import Rake


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


    # TODO: THE ML Stuff should be moved to separate class
    def generateKeyWordsYake(self):
        text = self.getAllText()
        deduplicationThreshold = 0.9
        language = "en"
        maxLengthOfKeyword = 2
        numOfKeywords = 10
        features = None

        keywordExtractor = yake.KeywordExtractor(
            lan=language, n=maxLengthOfKeyword, dedupLim=deduplicationThreshold, top=numOfKeywords, features=features
        )
        keywords = keywordExtractor.extract_keywords(text)

        return keywords
    
    def generateKeywordsRake(self):
        text = self.getAllText()
        rake = Rake()
        rake.extract_keywords_from_text(text)
        keywords = rake.get_ranked_phrases()
        return keywords[:10]
        

    def test(self):
        print(self.getAllText())
        return self.generateKeywordsRake()
