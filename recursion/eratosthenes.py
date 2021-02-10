def sieve(start, finish):
  primes = []
  res = []
  for i in range(2, finish + 1):
    primes.append(i)


  for n in primes:
    
    if n ** 2 > finish:
      for num in primes:
        if num >= start:
          res.append(num)
        else:
          continue
      return res
    
    for num in primes[n * 2:]:
      if num % n == 0:
        primes.remove(num)
 
