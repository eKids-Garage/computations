# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
from math import sqrt
def is_prime(N):
  for X in range(2, int(sqrt(N)) + 1):
    if N % X == 0:
      print("NO")
      return
  print("YES")

is_prime(9)
is_prime(7)
is_prime(37)
is_prime(37*71)