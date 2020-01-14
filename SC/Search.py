import nltk
from nltk import *
#nltk.download('averaged_perceptron_tagger')
file = open("a.txt")
text = file.read()
print (text)
#text="some text"

regularexpression=r""

searchtext="some text"#some text that you wanna search in text


def SearchRegularExpression(text, regularexpression):#this method return the number of found 
    
    match = re.findall(regularexpression, text)
    if(match):
        return len(match.group())
    else:
        return("not found")


# this method return a list of matched text
def SearchRegularExpression(text, regularexpression):

    match = re.findall(regularexpression, text)
    if(match):
        return (match.group())
    else:
        return("not found")
    
######################################################################################

def findverb(text):
#VB verb, base form take #VBD verb, past tense took #VBG verb, gerund/present participle taking #VBN verb, past participle taken #VBP verb, sing. present, non-3d take #VBZ verb, 3rd person sing. present takes
    verbtag=["VB","VBD","VBG","VBN","VBP","VBZ"]# verb tag in EN
    inTAG = ["TO", "JJ", "IN"]  # infinitive tags in EN
    import Tokenize #Using Tokenize module 
    tokenized_sent = Tokenize.SentenceTokenize(text)
    #print(tokenized_sent)
   # print("************************************************")
    verbs = ()
    verbin=[]
    for sent in tokenized_sent:
        tokenized_text = Tokenize.WordTokenize(text)  # tokenize words in text
        tagged_text = pos_tag(tokenized_text)  # POS using NLTK pos tagger
        #print(tagged_text)
        #print("************************************************")
        for i in range(len(tagged_text)):  # search between all word in text
            if(tagged_text[i][1] in verbtag):  # find all verbs
                if(tagged_text[i+1][1] in inTAG):  # find all verbs that have infinitive
                    #print(tagged_text[i][1])
                    #collect all verbs in a list named verbs
                        verbs = verbs+(tagged_text[i],)
                        verbs=verbs+(tagged_text[i+1],)
                        verbin.append(tagged_text[i][0]+" "+tagged_text[i+1][0])
                        
    return verbin#return the final list of verbs and tags
#Using function findverb()
print("************************************************")
print(findverb(text))


