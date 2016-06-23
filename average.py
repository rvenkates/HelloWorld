# average.py

def average(seq):

   total = 0
   for i in seq:
      total += i
      
   return(total/len(seq))

xs = [1,2,3,4,5]
print 'The average of ', xs, 'is', average(xs)
