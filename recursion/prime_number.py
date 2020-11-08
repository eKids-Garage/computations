# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
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