from nltk import *
text="Some text"#Get Text


#Delete Unwanted Digits
def DeleteDigit(text):
    unwanted = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for digit in unwanted:
        text=text.replace(digit, " ")


#Delete Unwanted Alphabets
def DeleteAlphabet (text):
    unwanted=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for alphabet in unwanted:
        text=text.replace(alphabet, " ")


#Delete Unwanted characters
def DeleteCharacter (text):
    unwanted = ['"', "'", '=', '@', '&', '%', '.', ',', ':', '\\', '$', '^', '<', '>', '!', '?','{', '}', ';', '\\n', '\\t', '(', ')', '[', ']', '/', '*', '+', '#', '\u200c', '\ufeff', '-', '_', '|']
    for char in unwanted:
        text=text.replace(char," ")
