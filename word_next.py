from collections import defaultdict
import random

chain = defaultdict(list)
with open('notes/hamlet.txt') as f:
    for line in f:
        last = None
        for word in line.split():
            chain[last].append(word)
            last = word

word = random.choice(chain.keys())
print word
while word [-1] not in '.!?':
    word = random.choice(chain[word])
    print word,
