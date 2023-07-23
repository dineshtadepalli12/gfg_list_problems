a = [20,5,19,22,10,1]
s = a[0]
for i in range(len(a)):
    if (a[i]<=s):
        s = a[i]
print(s)
#m2
a = sorted(list(a))
print(a[0])
#m3
print(min(a))