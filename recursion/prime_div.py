def prime_div(N, k):
  if N == 1:
    return k 
  else:
    if N % k ==0:
      print(k)
      N = N // k
    if N % k != 0:
      k = k+1
  prime_div(n,k)

prime_div(144404043420,2)