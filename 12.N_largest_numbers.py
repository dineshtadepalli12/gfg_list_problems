#you need to print the N largest elements in a list 
N=2
a = [81, 52, 45, 10, 3, 2, 96] 
b = list(set(a))
b.sort()
print(b)
print(b[-N:])
