N = int(input("Введи число  : "))

def prime_div(N, K = 2):
  if N == K :  # n%k !=0 не работает правильно
    print(K)
    return
  elif N % K == 0:
    print(K)
    prime_div(N // K, K)
  else:
    prime_div(N, K + 1)

prime_div(N)