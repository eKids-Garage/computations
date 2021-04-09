# Напишите функцию, которая складывает два рациональных числа
# Структуру данных для хранения чисел выберите и реализуйте сами

def gcd (a,b):
  if a != b:
    if a > b:
      a -= b
    else:
      b -= a
    return gcd(a,b)
  else:
    return b

def sum_rat(a, b):
  n = a[0] * b[1] + b[0] * a[1]
  d = a[1] * b[1]
  e = gcd(n,d)
  n = n // e
  d = d // e
  if (n // d) > 1:
    p = n // d
    n = n - p * d
    print(p,n,'/',d)
  else:
    print(n,'/',d)


#первое число
a = [5,13]
#второе число
b = [15,3]
sum_rat(a,b)
