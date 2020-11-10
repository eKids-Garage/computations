# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  
N = int(input("введите число "))
def prime_div(n, k):
  if n // k >= k:
    if n % k == 0:
      print(k)
      n = n // k
    else: 
	    k = k + 1
    prime_div(n, k)

  else:
    print(n)


prime_div(N, 2)  