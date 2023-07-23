#swapping the first elemnets of the list

def swapping(list1,n):
    temp = list1[0]
    list1[0]= list1[n-1]
    list1[n-1] = temp
    return list1

#driver code
list = [1,2,3,4,5]
n = len(list)
print(swapping(list,n))

#method2

def swaplist(list2):
    list2[0],list2[-1] =list2[-1],list2[0]
    return list2

#driver code
print(swaplist([1,2,3,4,5]))