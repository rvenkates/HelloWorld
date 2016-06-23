# variable.py

x = 'This is a very very long Python String.'
print x
print len(x)
print type(x)
z = 'This is a very very long Python String.'
y = x

print y

print x == y #Checking got equality
print x == z
print x is y #Checking for identity
print x is z

x = {1,2,3}
y = x
z = {1,2,3}

# if x == y          (does NOT imply)    x is y
# if id(x) == id(y)  (always implies)    x is y
#if x is y           (usually implies)   x == y
