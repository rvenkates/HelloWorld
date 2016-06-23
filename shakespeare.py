from collections import Counter


counts = Counter()
with open('notes/hamlet.txt') as f:
    for line in f:
            counts.update({word: counts.get(word, 0) + 1 for word in line.split()})

            
