# Реши задачу Иосифа Флавия:
# где n - число солдат, k - шаг (2 - каждый второй (сосед), 3 - каждый третий и т.д.)
# 
# 1. survive(n, k) - используя массив. 
# 2. survive_num(n, k) - без использования массива 

n = int(input())
k = int(input())

def survive(n, k, i = 0):
  warriors = []

  if not i:
    warriors = [j for j in range(1,n+1)]
  if len(warriors) < 2:
    return warriors
  warriors.remove(warriors[(i + k - 1) % len(warriors)])
  return survive(n, k, i+1)


print(survive(n,k))

def survive_num(n, k):
  if n == 1:
    return 1
  return 1 + ((survive_num(n-1, k) + k - 1) % n)


print(survive_num(n,k))



  
