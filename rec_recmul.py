def rec_mul(a, b):
  n=0
  x=a
  while x>0:
    x=x//10
    n=n+1
  if n==1:
    return a*b
  else:
    pol1=a//(10**(n/2))  
    pol2=a%(10**(n/2)) 
    pol3=b//(10**(n/2))
    pol4=b%(10**(n/2)) 
    res1=rec_mul(pol2,pol4) 
    res2=rec_mul(pol1,pol4)
    res3=rec_mul(pol2,pol3)
    res4=rec_mul(pol1,pol3)
  return res1+res2*(10**(n/2))+(res3+res4*(10**(n/2)))*(10**(n/2))

print(rec_mul(1234,5678))  