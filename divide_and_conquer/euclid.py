# Реализуйте алгоритм Евклида с помощью рекурсии
def euclidus(n1, n2):
  if n2%n1 == 0:
    return n1
  return euclidus(n2%n1, n1)

print(euclidus(1000, 300))