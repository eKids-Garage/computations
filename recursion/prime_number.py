
import math
def is_prime(N):
  k = 2
  i = math.sqrt(N)
  while (k <= i):
    if N % k == 0:
      return 0
    k += 1
  return 1


N = int(input())
if is_prime(N) == 1:
  print ("YES")
else:
  print ("NO")
