# Реши задачу Иосифа Флавия:
# где n - число солдат, k - шаг (2 - каждый второй (сосед), 3 - каждый третий и т.д.)
# 
# 1. survive(n, k) - используя массив. 
# 2. survive_num(n, k) - без использования массива 

def survive(n, k):
  a = list(range(1,n + 1))
  while len(a) > k - 1:
    b = []
    i = 0
    n = len(a)
    print("round:")
    while i < n:
      m = min(i+k-1, n)
      print(a[i:m+1])
      if i+k < n:
        b += a[i:m]
      else:
        b = a[i:m] + b
      i += k
    print(b)
    a = b
  return a

print(survive(9,2))
# print(survive(16,3))

def survive_num(n, k):
    pos = 0
    
    return pos