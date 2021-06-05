from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


import json

words=[]

with open('intents.json') as file:
    data=json.load(file)
for intent in data['intents']:
    for pattern in intent['patterns']:
        wrds=word_tokenize(pattern)
        words.extend(wrds)
        #print(word_tokenize(pattern))
words=[stemmer.stem(w.lower()) for w in words]
words=sorted(list(set(words)))
print(words)
