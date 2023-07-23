start = 4
end = 15
b = []
for i  in range(start,end):
    if i%2==0:
        b.append(i)
print(b)

#method 2 using list comprehension

res = [i for i in range(start,end) if i%2==0]
print(*res)

#method 3 using recursion
 
def even(num1,num2):
    if num1>num2:
        return
    print(num1,end=" ")
    return even(num1+2, num2)

n1=4
n2=16
even(n1,n2)
