# Написать программу, которая находит все простые числа в заданном 
# интервале методом "Решето Эратосфена". 
# start и finish - границы диапазона (включительно).
start = int(input())
finish = int(input())


def sieve(start, finish):
  array = [i for i in range(start, finish+1)]


  for j in range(2, finish//2):
    c = j
    if j != 2 and j % 2 == 0:
        j +=1
    else:
        while c + j <= finish:
          c += j
          array[c-1] = 0


  primes = []    
  for h in range(start, finish):
    if array[h]!= 0:
      primes.append(array[h])

  return primes


print(sieve(start,finish))
