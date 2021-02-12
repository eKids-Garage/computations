# Реши задачу Иосифа Флавия:
# где n - число солдат, k - шаг (2 - каждый второй (сосед), 3 - каждый третий и т.д.)
# 
# 1. survive(n, k) - используя массив. 
# 2. survive_num(n, k) - без использования массива 

def survive(n, k):
    return []

n = int(input('Число солдат:'))
k = int(input('Шаг:'))

def survive_num(n, k):
  if n == 1:
    return 1
  return 1 + (survive_num(n-1, k) + k - 1) % n
print('Место под номером ', survive_num(n, k))
