import math

def is_prime_tail(N, div):
  if (N%div == 0) and (div <= math.sqrt(N)):
    print('NO')
  elif (div == N):
    print('YES')
  else:
    div = div + 1
    is_prime_tail(N, div)


def is_prime_tail_while(N, c):

  while N > c:
    if ((N % c) == 0) and (c <= math.sqrt(N)): 
      print ('NO')
      break

    c = c + 1

    if c == N:
      print ('YES')
      break
