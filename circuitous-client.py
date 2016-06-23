'''
Our customers' code.
'''

from circuitous import Circle

# Customer 1: our academic friends
import random

print 'Proposal to research the areas of random circles'
print 'using Circuitous (tm)', Circle.version
n = 3
random.seed(42)
print 'the average area of', n, 'random circles'
print 'seeded on the Answer to Life, the Universe, and Everything'
circles = (Circle(random.random()) for i in xrange(n))
areas = (c.area() for c in circles)
print 'is %.2f' % (sum(areas) / n)
print

# Customer 2: Local rubber sheet company
cuts = [0.7, 0.3, 0.5]
circles = [Circle(radius) for radius in cuts]

for c in circles:
    print 'A circle with radius', c.radius
    print 'has an cold area %.2f' % c.area()
    print 'and a perimeter %.2f' % c.perimeter()
    c.radius *= 1.1
    # Java: c.set_radius(c.get_radius() * 1.1)
    print 'and a warm area %.2f' % c.area()
    print

# Customer 3: Regional tire company

class Tire(Circle):

    def perimeter(self):
        'Perimeter adjusted for width of tire'
        return Circle.perimeter(self) * 1.25

t = Tire(22)
print 'a tire with radius', t.radius
print 'has an area %.0f' % t.area()
print 'and a perimeter %.0f' % t.perimeter()
print

# Customer 4: national trucking company
print 'a hill with inclinometer reading 7 degrees'
print 'is a percent grade: %.2f%%' % Circle.angle_to_grade(7)
print

# Customer 5: international graphics company
# We have money and power!
# We want the constructor to be based on the bounding box diagonal!
c = Circle.from_bbd(10)
print 'a circle with a bounding box diagonal 10'
print 'has a radius %.2f' % c.radius
print 'and an area %.2f' % c.area()
print

# Customer 6: the Feds
# We like to micromanage:
# we will tell you not just WHAT to do, but also HOW to do it

# ISO-10666-fake
# Thou shalt not create area methods that directly access the radius
# Instead you must infer the radius from the perimeter

# ISO-10667
# Circle classes must not store the radius
# Circle classes must store the diameter and ONLY the diameter

print 'federal inspection'
c = Circle(10)
print c.__dict__
print c.area()
c.radius = 20
print c.__dict__
