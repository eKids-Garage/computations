# Напишите функцию, которая складывает два рациональных числа
# Структуру данных для хранения чисел выберите и реализуйте сами
z1 = int(input('Знаменатель первого числа:'))
h1 = int(input('Числитель первого числа:'))
z2 = int(input('Знаменатель второго числа:'))
h2 = int(input('Числитель второго числа:'))
x = [h1, z1]
y = [h2, z2]
def sum_rat(a, b):
  z = a[1]*b[1]
  h = a[0]*b[1]+a[1]*b[0]
  k = 1
  if z > h:
    small = h
  else:
    small = z
  while k < small:
    if z % k == 0 and h % k == 0:
      z = z/k
      h = h/k
    k = k + 1
  return [h, z]
print(sum_rat(x, y))