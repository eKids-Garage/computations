# Реализуйте алгоритм Евклида с помощью рекурсии
def euclidus(n1, n2):
  if n2%n1 == 0:
    return n1
  return algo(n2%n1, n1)

print(algo(1000, 300))