# Написать программу, которая находит все простые числа в заданном 
# интервале методом "Решето Эратосфена". 
# start и finish - границы диапазона (включительно).
import math
set=[]
primes=[]

def sieve(start, finish):
  if (start==1):
    sieve(2,finish)
  if start<math.sqrt(finish):
    if set==[]:
      for i in range (start, finish+1):
        set.append(i)
    
    if start!=0:
     for n in range (2*start-1, finish, start): 
       set[n-1]=0
     sieve(start+1,finish)
  else:
    for t in range(0, finish-1):
      if set[t]!=0:
        primes.append(set[t])
    print(primes)

sieve(2,100000)

#works much better with sqrt than with finish/2. for /2 recursion crashes at 500(even less) and with sqrt only at 10000000