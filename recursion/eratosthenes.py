# Написать программу, которая находит все простые числа в заданном 
# интервале методом "Решето Эратосфена". 
# start и finish - границы диапазона (включительно).

start = int(input('Начало отсчета:'))
finish = int(input('Конец отсчета:'))

def sieve(start, finish):
  i = start
  mass = []
  while i < finish + 1:
    mass.append(i)
    i = i + 1
  for p in mass:
    def is_prime(n, c = 2):
      if c > int(n**0.5) :
        r = "YES"
        return r
      if n % c == 0:
        r = "NO" 
        return r
      return is_prime(n, c + 1)
    z = is_prime(p)
    print(z)
    if z == "NO":
      v = mass.index(p)
      mass[v] = 0
      continue
  primes = []
  for x in mass:
    if x!= 0:
      primes.append(x)
  return primes

print(sieve(start, finish))