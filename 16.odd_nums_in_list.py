def odd_list(start,end):
  a = []
  for i in range(start,end+1):
    if i%2!=0:
      a.append(i)
  return a 

if __name__=="__main__":
  print(odd_list(0,10))
