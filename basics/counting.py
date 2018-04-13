import nltk
import pprint

pprint.pprint(nltk.corpus.gutenberg.fileids())

md = nltk.corpus.gutenberg.words("melville-moby_dick.txt")
md_sents = nltk.corpus.gutenberg.sents("melville-moby_dick.txt")
print(md_sents[3])