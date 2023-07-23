#finding the second largest element in the list 
#method 1 

list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]
list2 = list(set(list1))
list2.sort()
#print(list2)
print(list2[-2])


#method 2 
#by removing the max element in the list and then printing the max element. 

a = [10, 20, 20, 4, 45, 45, 45, 99, 99]

b = list(set(a))
b.remove(max(b))
b.sort()
print(b[-1])

#method 3 
c = set(a)
print(sorted(c)[-2])
