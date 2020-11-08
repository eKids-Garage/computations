# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  
def prime_div(N, k=2):
  if (k>n)/2:
    return
  elif (N//k==N/k):
    print (k)
    prime_div(N/k, k)
  else: 
    prime_div(N, k+1)
N=int(input())
n=N
prime_div(N)
