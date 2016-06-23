'''
Creating and solving a race condition.

Race conditions:
    1. pop from an empty queue
    2. early exit from the consumer
    3. early termination of program
'''
from collections import Counter
from threading import Thread
import re, time

### Serial #################################################
print 'SERIAL, CORRECT'
counts = Counter()
with open('notes/hamlet.txt') as f:
    for line in f:
        for word in re.findall(r'[a-z]+', line.lower()):
            counts[word] += 1

print counts.most_common(5)

### Parallel ###############################################

counts = Counter()
q = []

def producer(filename):
    with open(filename) as f:
        for line in f:
            for word in re.findall(r'[a-z]+', line.lower()):
                q.append(word)

def consumer(q):
    while True:
        try:
            word = q.pop()
        except IndexError:
            time.sleep(1)
        else:
            counts[word] += 1

filenames = ['notes/hamlet.txt']
producers = [Thread(target=producer, args=(name,)) for name in filenames]
for t in producers:
    t.start()

for i in range(2):
    t = Thread(target=consumer, args=(q,))
    t.daemon = True
    t.start()

for t in producers:
    t.join()
while q:
    time.sleep(1)

print 'PARALLEL'
print counts.most_common(5)
        
