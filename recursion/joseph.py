# Реши задачу Иосифа Флавия:
# где n - число солдат, k - шаг (2 - каждый второй (сосед), 3 - каждый третий и т.д.)
# 
# 1. survive(n, k) - используя массив. 
# 2. survive_num(n, k) - без использования массива 
surv=[]
def survive(n, k):
  for i in range (0, n):
    surv.append(i+1)
  for j in range (k-1,n-1,k):
    for a in range (0, k-1):
      if surv[j+a]!=0:
        surv[j+a]=0
        break
  for j in range (k-1,n-1,k):
    for a in range (0, k-1):
      if surv[j+a]!=0:
        surv[j+a]=0
        break
  print(surv)

    

    


def survive_num(n, k):
    pos = 0
    
    return pos
    
survive(3, 2)


