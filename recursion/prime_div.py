
def prime_div(N):
  k = 2
  while (N % k != 0):
    k += 1
  return k


N = int(input())
k = prime_div(N)
print (k)
while (N > 1):
  N = N / k
  k = prime_div(N)
  print (k)
  