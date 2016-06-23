# comprehension.py

from __future__ import division # "pragma"
import math

xs = [1, 2, 3, 50, -10, -5000]
 
print 'task 1: calculates the average of xs'

def average(seq):
    return sum(seq) / len(seq)
 
print average(xs)

print 'task 2: calculate the minimum value in xs = -5000'
print min(xs)
print 'task 3: calculate the maximum value in xs = 50'
print max(xs)

print 'task 4: calculate the min magnitude (abs val) in xs = 1'
print min(xs, key=abs)
print 'task 5: calculate the max magnitude (abs val) in xs = -5000'
 
 
print 'task 6: calculate the number in xs which has the most 1s in its binary representation'
def num_ones(x):
    return(bin(x).count('1'))
print max(xs, key=num_ones)

print 'task 7: calculate the variance & standard deviation of xs'
def deviation(x, a):
    return (x-a) ** 2

v = []
av = average(xs)
for x in xs:
    v.append(deviation(x, av))

var = average(v)

print var
        
