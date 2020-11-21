def sum(N):

  a=N%10
  N=N//10  

  if(N==0):
    return a 

  else:
    return a+sum(N)



def sum_tail(N, res):
  
  a=N%10
  N=N//10  
  res=res+a 

  if(N==0):
    return res

  else:
    return sum_tail(N,res)


def sum_tail_while(N):
  res = 0
  while (N != 0):
    a = N % 10
    N=N//10
    res=res+a  
    
  print (res)
