# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  

def prime_div(N):
  k = 2
  while (N % k != 0):
    k += 1
  return k


N = int(input())
k = prime_div(N)
print (k)
while (N > 1):
  N = N / k
  k = prime_div(N)
  print (k)