# Написать программу, которая находит все простые числа в заданном 
# интервале методом "Решето Эратосфена". 
# start и finish - границы диапазона (включительно).

import math

def sieve(start, finish):
  wow = [True for i in range(2, finish + 1)]
  i = 0
  while (i + 2) ** 2 < finish:
    if wow[i]:
      j = (i + 2) ** 2 - 2
      while j < len(wow):
        print(j+2, "is not")
        wow[j] = False
        j += (i + 2)
    i+=1
  primes = []
  for i, isPrime in enumerate(wow):
    if isPrime and i + 2 >= start:
      primes.append(i+2)
  return primes
  


print(sieve(7, 23))
