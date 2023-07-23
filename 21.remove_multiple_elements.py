#1 remove all the even numbers from a list 
from functools import reduce
list1 = [11, 5, 17, 18, 23, 50]
result = list(filter(lambda a: (a%2==0), list1))
print(result)

#2 using the list comprehension
result2 = [ele for ele in list1 if ele%2==0]
print(result2)
#3 using nested loops
c=[]
for ele in list1:
    if ele%2==0:
      c.append(ele)
print(c)