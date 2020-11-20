# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def dividors(n):
    return 0

#не знаю как сделать обычную рекурсию

def dividors_tail(n, k):
  if n / k == 1:
    print(k)
  else:
    if n % k == 0:
      print(k)
      dividors_tail(n / k, k)
    else:
      dividors_tail(n, k + 1)

n = int(input("Number:"))
k = 2
dividors_tail(n, k)

while n / k != 1:
  if n / (k + 1) == 1:
    print(k + 1)
    k = k + 1
    n = n / k
  else:
    if n % k != 0:
      k = k + 1
    else:
      n = n / k
      print(k)