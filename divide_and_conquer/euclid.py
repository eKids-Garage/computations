# Реализуйте алгоритм Евклида с помощью рекурсии
a = int(input("Введите число:"))
b = int(input("Введите число:"))
def euclidus(a, b):
  if a == b:
    return a
  elif a > b:
    a = a - b
  elif a < b:
    b = b - a
  return euclidus(a, b)
print('Квадрат со тороной ', euclidus(a, b))

