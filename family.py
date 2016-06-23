# family.py
 
# Homer    J       male     Apr-12    sports, boats
# Marge          female     May-21    computers, planes
# Bart             male     Sep-13    cars, planes, boats
# Lisa           female     Jun-9     
 
family = [
    ('Homer', 'J', 'male',   4, 12, {'sports', 'boats'}),
    ('Marge',  '', 'female', 5, 21, {'computers', 'planes'}),
    ('Bart',   '', 'male',   9, 13, {'cars', 'planes', 'boats'}),
    ('Lisa',   '', 'female', 6, 9,  set()),
]
 
def as_str(family):
    body = []
    line_template = '%-15s (%d-%d) %s'
    for firstname, middle, gender, month, day, interests in family:
        line = line_template % (firstname, month, day, ', '.join(interests))
        body.append(line)
    return '\n'.join(body)
 
html_template = '''
<html>
    <head>
        <title>Our Family</title>
    </head>
    <body>
        <ul>
%s
        </ul>
    </body>
</html>'''
member_template = '''
    <li>%s (%d-%d): %s</li>
'''

def as_html(family):
    body = []
    for firstname, middle, gender, month, day, interests in family:
        body.append(member_template % (firstname, month, day, ', '.join(interests)))
    print html_template % (''.join(body))  
