# crossword.py

import re

filename = 'notes/words.txt'
 
with open(filename) as f:
    wordlist = { line.strip().lower() for line in f if line.strip() }

def find_crossword_candidates(wordlist, entry):
    pattern = '^' + entry.replace('_', '.') + '$'
    candidates = {word for word in wordlist if re.search(pattern, word)}
    return candidates

match_words = find_crossword_candidates(wordlist, 'f__d')

print match_words


