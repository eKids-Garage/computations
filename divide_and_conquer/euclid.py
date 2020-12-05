# Реализуйте алгоритм Евклида с помощью рекурсии

A = int(input())
B = int(input())

def euclidus(a, b):
  while a != 0 and b != 0:
    if a > b:
      a = a % b
    else:
      b = b % a
  print(a + b)

euclidus(A,B)