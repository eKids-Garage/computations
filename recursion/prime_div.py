
N = int(input("Введи число  : "))

def prime_div(N, K = 2):
  if N == K :  # n%k !=0 не работает правильно
    return K
  elif N % K == 0:
    print(K)
    return prime_div(N // K, K)
  else:
    return prime_div(N, K + 1)

print(prime_div(N))
