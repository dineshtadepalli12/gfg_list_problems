ist = [4, 5, 6, 7, 8, 9]
ist.append(10)
print(ist[::-1])

#method 2
a = []
for i in range(len(ist)-1,-1,-1):
    a.append(ist[i])
print(a)
ist.reverse()
print(ist)
