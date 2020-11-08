# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  

def prime_div(n, k = 2):
  if n == k:
    print(k)
    return
  elif n % k == 0:
    print(k)
    prime_div(n // k, k)
  else:
    prime_div(n, k + 1)

"""prime_div(24)
prime_div(5)
prime_div(2)
prime_div(3)
prime_div(4)
prime_div(56)
prime_div(8)"""