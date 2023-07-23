def positive_range(start,end):
    li = []
    for i in range(start,end+1):
        li.append(i)
    a = list(filter(lambda x:(x>0),li))
    return a 
print(positive_range(-3,5))

#can also be done using list comprehension, traditional loop etc. 

