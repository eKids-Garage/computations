#реализовать алгоритм с использованием обычной рекурсии у меня не получилось

def is_prime_tail(N, c):
  c = c + 1
  if N % c == 0:
    if c != N:
      return "NO"
    else:
      return "YES"
  else:
    if c > N / 2:
      return "YES"
    else:
      return is_prime_tail(N, c)

def is_prime_while(N):
  c = 1
  while c <= N / 2:
    c = c + 1
    if N % c == 0:
      if c != N:
        return "NO"
      else:
        return "YES"
    else:
      if c > N / 2:
        return "YES"


N = int(input("Input any number: "))
c = 1
print(is_prime_tail(N, c))
print(is_prime_while(N))
