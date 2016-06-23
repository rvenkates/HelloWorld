''' Copyright (c) 2016 Circuitous, Inc.

Eric Ries, "Lean Startup Method"
Lean Startup : Business Plans :: Agile : Waterfall
He likes to say, "get out of the building"
    Share a Minimum Viable Product (MVP)

YAGNI: Ya Ain't Gonna Need It
       You are not going to need it


bound method
    typical instance method call:   instance.method()
    passes the instance as the implicit first argument, usually 'self'

unbound method
    a method called from the class:     ClassName.method(instance)
    needs an explicit instance passed as the first argument

static method
    a method called from the class:     ClassName.method()
    that does not require an instance as the first argument

class method
    a method called from the class:     ClassName.method()
    that implicitly passes in the class as the first argument
    this is useful for alternate constructors

the open/closed principle
    a class should be open for extension (method overrides)
    but closed for modification (an override of one method
    should ONLY change the behavior of that method, no others)

name mangling
    prefixing an attribute/method name with two underscores:  __name
    the interpeter will compile your class object
    and mangle the name with the class name as a prefix:  _Class__name
    This is useful for keeping an extra reference to
    helper methods so that you follow the open/closed principle
'''

import math
from collections import namedtuple

Version = namedtuple('Version', 'major minor patch')

class Circle(object):
    'An advanced circle analytics toolkit'

    version = Version(0, 3, 1)

    def __init__(self, radius):
        'most people do not see the docstrings on magic methods'
        self.radius = radius

    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    # radius = property(get_radius, set_radius)

    @classmethod
    def from_bbd(cls, bbd):
        'create a new Circle from a bounding box diagonal'
        radius = bbd / math.sqrt(2)
        return cls(radius)


    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.radius)

    def area(self):
        'Perform quadrature on a planar shape of uniform revolution.'
        radius = self.__perimeter() / math.pi / 2.0
        return math.pi * radius ** 2

    def perimeter(self):
        '''
        Compute a closed line intergral for the locus of points
        equidistant from a given point.
        '''
        return math.pi * self.radius * 2

    __perimeter = perimeter
    

    @staticmethod
    def angle_to_grade(angle):
        'Convert an inclinometer reading from degrees to percent-grade'
        return math.tan(math.radians(angle)) * 100.0
