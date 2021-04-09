# Напишите функцию, которая складывает два рациональных числа
# Структуру данных для хранения чисел выберите и реализуйте сами
n1 = int(input("write numerator 1 - "))
d1 = int(input("write denaminator 1 - "))
n2 = int(input("write numerator 2 - "))
d2 = int(input("write denaminator 2 - "))
a = [n1,d1]
b = [n2,d2]

def sum_rat(a, b):
  s = a[0] * b[1] + b[0] * a[1]
  p = a[1] * b[1]
  print(s,p)
  e = euclidus(s, p)
  print(e)
  s = s // e
  p = p // e
  print("answer:", s,p)

def euclidus(a, b):
  print(a, b)
  if a != b:    
    if a > b:
      a -= b
    else:
      b -= a
    return euclidus(a,b)

  else:
    return b
    
sum_rat(a, b)