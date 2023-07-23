def negative_range(start,end):
  a = []
  for i in range(start,end+1):
    a.append(i)
  result = list(filter(lambda b : b<0,a))
  return result
print(negative_range(-5, 3))
