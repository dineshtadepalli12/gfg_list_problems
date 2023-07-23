a = [20,5,19,22,10,1]
l = a[0]
for i in a:
    if(i>=l):
        l = i
print(l)
#m2
b=(sorted(list(a)))
print(b[-1])
print(max(a))