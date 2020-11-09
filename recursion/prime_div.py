# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  
N = input("Введите число:")
def prime_div(n, k = 2):
  if n % k < k:
    return
  if n % k == 0:
    print(k)
    return prime_div(n//k, k)
  if n % k != 0:
    return  prime_div(n, k + 1)
print(prime_div(N))