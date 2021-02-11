# Реши задачу Иосифа Флавия:
# где n - число солдат, k - шаг (2 - каждый второй (сосед), 3 - каждый третий и т.д.)
# 
# 1. survive(n, k) - используя массив. 
# 2. survive_num(n, k) - без использования массива 



surv=[]
def survive(n, k, j=0):
  if surv==[]:
    for i in range (0, n):
      surv.append(i+1)
      j=k
  count=0
  sortsurv=[]
  for i in range (0,n):
    if not surv[i]==0:
      count=count+1
      sortsurv.append(surv[i])
  if count==1:  
    print (sortsurv) 
  else:
    for a in range (0,n):
      if not surv[a]==0:
        if j==1:
          surv[a]=0
          j=k
        else:
          j=j-1
    survive(n,k,j)

    
survive(10,3)
 
  


    

    


def survive_num(n, k):
    pos = 0
    
    return pos
    

