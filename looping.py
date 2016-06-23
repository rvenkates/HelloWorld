# looping.py

colors = 'red blue yellow yellow green turquoise red chartreuse purple'

print '\nTask 1'
for color in colors.split():
    print color.capitalize()

print '\nTask 2'
for index, color in enumerate(colors.split()):
    print index, color.upper()

print '\nTask 3'

color_set = set(colors.split())

for color in sorted(color_set):
    print color

print '\nTask 4'
from collections import Counter

hist = Counter(colors.split())
for color, count in sorted(hist.items()):
    print color, count

print '\nTask 5'
animals = 'tiger lion bear monkey rabbit hippopotamus rhino ox'

for animal in sorted(animals.split()):
    print animal

print '\nTask 5a'
for animal in sorted(animals.split(), key=len, reverse=True):
    print animal

print '\nTask 6'

colors = 'orange yelloe black brown grey pink grey maroon'
sizes = ' medium big big small tiny huge huge big'

for animal, color, size in zip(animals.split(), colors.split(), sizes.split()):
    print animal, color, size

print '\nTask 7'
animal_colors = {animal: color for animal, color in zip(animals.split(), colors.split())}

print animal_colors

print '\nTask 8'

animals = 'zebra;owl;giraffe;monkey;lion;tiger;gorilla;hippopotamus'

def count_vowels(word):
    return sum([c in 'aeiou' for c in word])


for animal in sorted(animals.split(';'), key=count_vowels, reverse=True):
    print animal
    
