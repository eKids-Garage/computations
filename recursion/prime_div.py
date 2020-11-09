# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  
N = int(input("Введите число: "))

def prime_div(N, k):
  if N == 1:
    return 1 
  else:
    if N % k == 0:
      print (k)
      N = N // k
      return prime_div(N, k)
    else:
      k += 1
      return prime_div(N, k)   

print (prime_div(N, 2))  