
import string
import re

def word_count(phrase):
    wordcount={}
    split = re.split('[^0-9a-zA-Z\']', phrase)
    for word in split:
        word = word.lower()
        word.translate(None, string.punctuation)
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    wordcount.pop('',None)
    print str(wordcount)
    return wordcount
