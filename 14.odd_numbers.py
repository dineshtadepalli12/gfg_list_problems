list1 = [2, 7, 5, 64, 14]
a=list(filter(lambda x:x%2!=0,list1 ))
print(a)
b = []
for i in list1:
    if i%2!=0:
      b.append(i)
print(b)

