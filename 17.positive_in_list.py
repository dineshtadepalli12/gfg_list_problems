def positive_list(list1):
    a=[]
    for i in list1:
        if i>0:
          a.append(i)
    return a 
print(positive_list([12, -7, 5, 64, -14]))    

#method 2 

list2 = [12, -7, 5, 64, -14]
b = [i for i in list2 if i>0]
print(b)

#method 3 using filter 

