# Написать программу, которая находит все простые числа в заданном 
# интервале методом "Решето Эратосфена". 
# start и finish - границы диапазона (включительно).

def sieve(start, finish):
  i = 0
  primes = list(range(2,finish+1))
  while i < len(primes)//2:
    for j in range(i + primes[i], len(primes),primes[i]):
      primes[j] = 0
    i = i + 1
    while primes[i] == 0 and i < len(primes):
      i = i + 1  
  primes = [x for x in primes if x!=0]
  return primes

print(sieve(0,28))
