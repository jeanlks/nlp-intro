import nltk
import pprint
alice =  nltk.corpus.gutenberg.words("carroll-alice.txt")

alice_fd = nltk.FreqDist(alice)
print(alice_fd["Rabbit"])
pprint.pprint(alice_fd.most_common(10))