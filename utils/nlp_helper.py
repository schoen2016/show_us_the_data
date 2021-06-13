
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
import re


class NLPHelper:
    def __init__(self, remove_stopwords=False):
        self.rsw = remove_stopwords


    def token(self, text):
        text = re.sub(r'[^\w\s-]', '', str(text))
        text = re.sub(r"[-']", ' ', str(text))
        text = word_tokenize(text) 
        return text


    def removeStopwords(self, words):
        if words is None:
            return words
        
        if len(words) == 0:
            return words

        if self.rsw:
            stop_words = set(stopwords.words('english')) 
            x = [w for w in words if not w in stop_words]
            return x
        return text


    def token_rsw(self, text):
        x = self.token(text)
        return self.removeStopwords(x)
