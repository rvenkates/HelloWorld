# show_books.py
 
'''
    parse(filename or file-like-obj)    -> ElementTree document
    ET.getroot()                        -> root Element
    E.tag                               -> that element's tag
    E.attrib                            -> all the XML attributes (in a dict)
    E.get(attrib name)                  -> value for an XML attrib
 
    for child in E:                     -> all the immediate children of that Element
        print child
 
    E.find(xpath)                       -> find the first matching element
    E.findall(xpath)                    -> find all matching elements
 
XPATH:
 
    'tag'                      -> immediate child with the matching tag
    'tag/subtag'               -> immediate child of the immediate child with the matching subtag
    'tag//subtag'              -> any child of the immediate child
 
    '.'                        -> current element
    '..'                       -> parent element
    '*'                        -> all children
 
            '*[1]'              -> the first child (xpath counts starting from 1)
            '*[last()]'         -> the last child
            '*[pos() <=3]'      -> the first three children
            '*[@attr]'          -> the first child with this attr
            '*[@attr="value"]'  -> the first child with the matching attr/value pair
            '*[tag="text val"]' -> the first child with the matching text in the tag
'''
 
from xml.etree.ElementTree import parse
filename = 'notes/books.xml'
 
with open(filename) as f:
    catalog = parse(f).getroot()
 
 
print '\ntask 1: print all the book identifiers'

for bookid in catalog:
    print bookid.attrib

print '\ntask 2: show all the book titles'

for book in catalog.findall('book'):
    print book.find('title').text
print '\ntask 3: show author, publication date of bk105'

book = catalog.find('*[@id="bk105"]')
print book.find('author').text, book.find('publish_date').text

print '\ntask 4: show author, price of all computer books'

for book in catalog.findall('book'):
    if book.find('genre').text in ('Computer'):
        print book.find('author').text, book.find('price').text
        
print '\ntask 5: show all `metadata` for bk107'

book = catalog.find('*[@id="bk107"]')
print book.find('author').text, book.find('publish_date').text

print '\ntask 6: Most Expensive/Least Expensive/Total'

computer_books = []
for book in catalog.findall('book'):
    if book.find('genre').text in ('Computer'):
        computer_books.append((book.find('price').text, book.find('title').text))
        

    
print max(sorted(computer_books, reverse=True))
print min(sorted(computer_books, reverse=True))
 
