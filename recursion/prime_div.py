# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  

def prime_div(n, k):
  if k > n:
    print("The end")
  else:
    if n % k == 0:
      print(k)
      print(n / k)
      prime_div(n / k, k)
    else:
      prime_div(n, k + 1)

n = int(input("Number:"))
k = 2
prime_div(n, k)
    