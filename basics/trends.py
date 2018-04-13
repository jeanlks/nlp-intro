import nltk
from nltk.corpus import inaugural
import pprint
import pandas as pd


def takeFirst(elem):
    return elem[0]

for speech in inaugural.fileids():
    words_total = len(inaugural.words(speech))
   # print("Total words: {}, speech: {} ".format(words_total, speech))



speech_len = [(len(inaugural.words(speech)),speech ) for speech in inaugural.fileids()]
#pprint.pprint(speech_len)

dataset = pd.DataFrame([int(speech[:4]), len(inaugural.words(speech)), speech] for speech in inaugural.fileids())

dataset.columns = ["Year","Count words", "Speech"]
print(dataset)