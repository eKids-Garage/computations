# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  

def prime_div(N, k):
    if(N != 1):
      if (N % k == 0):
        N = N / k
        print(k)
        k = 2
        prime_div(N, k)
      else:
        k = k + 1
        prime_div(N, k)

N = int(input("Input any number: "))
k = 2
prime_div(N, k)
