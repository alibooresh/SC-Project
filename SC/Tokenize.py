import nltk
from nltk import *
from nltk.corpus import webtext


text="Some text"


def SentenceTokenize(text):
    #Train a tokenizer
    sent_tokenize(text)#this tokenizer is not trained 
    nltk.download("webtext")#download webtext for train a new tokenizer
    t= webtext.raw("overheard.txt")#use a text from webtext for train a new tokenizer
    from nltk.tokenize import PunktSentenceTokenizer
    my_tokenizer = PunktSentenceTokenizer(t)  # use PunktSentenceTokenizer for train a new tokenizer
    return my_tokenizer.tokenize(text)
def WordTokenize(text):
    from nltk.tokenize import WordPunctTokenizer
    #Use WordPunctTokenizer for tokenize words
    tokenizer = WordPunctTokenizer()
    return tokenizer.tokenize(text)
