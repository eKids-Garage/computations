# Реализуйте алгоритм Евклида с помощью рекурсии

a = int(input ("1 сторона: "))
b = int(input ("2 сторона: "))

def euclidus(a, b):
  if b > a :
    a , b = b , a
  if a%b == 0:
    return b
  else:
    return euclidus(a - ((a//b)*b), b)

print("максимальный квадрат: ", euclidus(a,b))

