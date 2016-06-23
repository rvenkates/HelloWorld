# strings.py
 
x = 'superman'
x = "clark kent"
 
# there is not difference ' and " in Python
 
print "Double quotes let us include 'single quotes' easily."
print '"Single quotes", I say authoritatively, "Are useful the other way around!"'
 
x = 'c'
print isinstance(x, str)
 
print '''
A mosquito did cry out in pain,
"A scientist's rotting my brain!"
The cause of his sorrow,
Was para-dichloro,
Diphenyl-tricholoroethane (DDT)
'''
 
print """
The mighty Thor,
He rode to war,
Upon his fine white filly.
"I'm Thor!" he cried;
The horse replied:
"Then wear a thaddle thilly!"
"""

print 'C:\\Users\travis\My Documents'
 
print '\tThis is shifted over a bit\n'
 
print r'C:\\Users\travis\My Documents'

def count_excl_ws(string):
   excl = 0
   for c in string:
       if ((c == ' ') or (c == '\t') or (c == '\n')):
           excl += 1
   return len(string) - excl
           
         
           

msg = 'This is a t    est  \t string \n'

print count_excl_ws(msg)


sentence = "Python is a great language to use at conpanies like cisco! or facebook!"
