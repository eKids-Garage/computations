# Написать программу, которая находит все простые числа в заданном 
# интервале методом "Решето Эратосфена". 
# start и finish - границы диапазона (включительно).

import math

def sieve(start, finish):
  primes = []
  for n in range(start, finish + 1):
    is_prime = True
    for p in range(2, round(math.sqrt(n)) + 1):
      if n % p == 0:
        is_prime = False
        break
    if is_prime:
      primes.append(n)
  return primes
start = int(input())
finish = int(input())
print(sieve(start, finish))