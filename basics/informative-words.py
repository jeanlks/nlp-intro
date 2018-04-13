import nltk

alice = nltk.corpus.gutenberg.words("carroll-alice.txt")
alice_fd = nltk.FreqDist(alice)
alice_fd_100 = alice_fd.most_common(100)
