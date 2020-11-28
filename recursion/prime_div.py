# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  

N = int(input())
k = 2
def divide(N, k):
  if N < k:
    return
  while N%k < k:
    if N%k == 0:
      print(k)
      return divide(N//k, k)
    else:
      return divide (N, k+1)

divide (N, k)
