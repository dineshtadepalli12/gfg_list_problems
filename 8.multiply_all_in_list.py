from functools import reduce
a = [5,2,3,4]
print(reduce(lambda x,y:x*y,a))
m = 1
for i in a:
    b = i*m
    m = b
print(m)
j=0
n = 1
while j<len(a):
    c = n * a[j]
    n = c
    j+=1
print(n)

import numpy
b = numpy.prod(a)
print(b)