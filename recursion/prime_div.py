# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  


def divide(N, k):
  if N > 1:
    if N % k == 0:
      print(k)
      divide(N / k, k)
    else:
      divide(N, k + 1)


print(divide(259,2))
  
 