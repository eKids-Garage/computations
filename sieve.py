numbers=[]
def sieve(start,finish):
  n=start
  while n<=finish:
    numbers.append(n)
    n += 1
    
  y=start
  ost=finish-start
  bround=0
  while y<=finish:
    minusone=0
    round=0
    x=1+bround #y2 #x1 #ost14
    while x<=ost:
      if numbers[x]%y==0:
        numbers.pop(x)
        ost=ost-1  
      x += 1  
    y=y+1
    bround += 1
  return numbers

print(sieve(2,16))