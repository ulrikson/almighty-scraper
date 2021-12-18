from requests import models
from HtmlParser import HtmlParser
import yake
from rake_nltk import Rake
import spacy


class KeywordGenerator:
    def __init__(self, text):
        self.text = text
        self.keywordCount = 10

    def generateWithYake(self):
        deduplicationThreshold = 0.9
        language = "en"
        maxLengthOfKeyword = 2
        features = None

        model = yake.KeywordExtractor(
            lan=language, n=maxLengthOfKeyword, dedupLim=deduplicationThreshold, top=self.keywordCount, features=features
        )
        keywords = model.extract_keywords(self.text)

        return keywords

    def generateWithRake(self):
        model = Rake()
        model.extract_keywords_from_text(self.text)
        keywords = model.get_ranked_phrases()
        return keywords[:self.keywordCount]

    def generateWithSpacy(self):
        model = spacy.load("en_core_web_sm")
        keywords = model(self.text).ents
        return keywords[:self.keywordCount]
