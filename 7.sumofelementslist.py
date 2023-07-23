from functools import reduce
a = [12, 15, 3, 10]
print(sum(a))
print(reduce(lambda x,y:x+y,a))
sum = 0
for i in range(len(a)):
    sum+=a[i]
print(sum)


