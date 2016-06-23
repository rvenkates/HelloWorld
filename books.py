# books.py
 
import json

 
filename = 'notes/books.json'
with open(filename) as f:
    catalog = json.load(f)  


print '\nTask 1'
for book in catalog:
    print book
    
print '\nTask 2'

print catalog["bk105"]['author'], catalog["bk105"]['publish_date']

print '\nTask 3'    
for book in catalog.values():
    print book['title']

print '\nTask 4'
for book in catalog.values():
    if book['genre'] == 'Computer':
        print book['author'], book['price']        

print '\nTask 5'
book = catalog['bk107']
for tag, text in book.items():
    print tag.upper()
    print text
