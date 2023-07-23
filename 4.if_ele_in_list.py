list1 = [1,2,3,4,5,6,7]
i=5
if i in list1:
    print(f"The element {i} exists")
else:
    print("It doesn't exist")

#method 2
list2 = [1,2,3,4,5,6,7]
j=7
for i in range(0,len(list2)):
    if list2[i] ==j:
        print(f"The element {j} exists")
        break
