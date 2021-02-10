# Реши задачу Иосифа Флавия:
# где n - число солдат, k - шаг (2 - каждый второй (сосед), 3 - каждый третий и т.д.)
# 
# 1. survive(n, k) - используя массив. 
# 2. survive_num(n, k) - без использования массива 

def survive(n, k, i = 0, arr= []):
  if not i:
    arr = [num+1 for num in range(n)]
  if len(arr) < 2:
    return arr
  arr.remove(arr[(i + k - 1)%len(arr)])
  return survive(n, k, i+1, arr)


def survive_num(n, k):
    pos = 0
    
    return pos
