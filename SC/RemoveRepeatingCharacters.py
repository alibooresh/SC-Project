from nltk.corpus import wordnet
import re
import nltk
nltk.download("wordnet")

text="some text"

class RepeatReplacer(object):
    def __init__(self):
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        self.repl = r'\1\2\3'

    def replace(self, word):
        if(wordnet.synsets(word)):
            return word
        repl_word = self.repeat_regexp.sub(self.repl, word)
        if(repl_word != word):
            return repl_wo.rd
            return self.replace(repl_word)
        else:
    

replacer = RepeatReplacer()
import Tokenize
Tokenize.text = text
words=Tokenize.WordTokenize(text)


for i in range(len(words)):
    replacer.replace(words[i])
