# numbers.py

from __future__ import division  # 'pragma' makes /- sign persorm true division

print 45 / 5

print 44 / 5         # True division

print 44 // 5        # Floor Division

print 2 ** 10
print 2 ** 100
print 2 ** 1000      # Python has arbitrary sized intregers (automatic promotion)

print 44 % 3         # Modulo

print divmod(44, 3)  # floor result + modulo

print abs(-41)

print oct(41)
print hex(41)
print bin(41)

print 4 * 4.0
print 4 + 4.0
print 4 / 4.0

print int (4 * 4.2)   # int * float) => float -> int
print  1/3 * 3
print 11 + 22 == 33
print 1.1 + 2.2 == 3.3   # imprecision due to decimal handling

print 4.0 == 4

print abs((1.1 + 2.2) - 3.3) < 0.1          # absolute threshold
print abs((1.1 + 2.2) - 3.3) < (0.1 * 3.3)  # relative threshold

x = 1 + 4j        # Imaginary numbers
y = 2 + 3j

print x + y

print x * y

print x + 2.0
print x + 2

print True, False

print type(10)
print type(10.0)
print type(10 + 1j)
print type(True)

print isinstance(10, int)
print isinstance(True, bool)
print isinstance(True, int)

xs = {True, False, False, True, True, True}
print sum(xs)

print 1 << 2
print 1 >> 2
print -1 >> 2
print 5 ^ 3
print 5 & 3
print 5 | 3
print ~5

x = 10
print hex(id(x))

x += 1
print hex(id(x))

x = x + 1 # x++ is incorrect for in place increment
print x
