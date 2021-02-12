# Реши задачу Иосифа Флавия:
# где n - число солдат, k - шаг (2 - каждый второй (сосед), 3 - каждый третий и т.д.)
# 
# 1. survive(n, k) - используя массив. 
# 2. survive_num(n, k) - без использования массива 

def survive_num(n, k):

n = int(input('Число солдат:'))
k = int(input('Шаг:'))

def survive(n, k):
  i = 1
  mass = []
  while i < n + 1:
    mass.append(i)
    i = i + 1
  number = 0
  count = 0
  while count < n-1:
    for element in mass:
      if element == 0:
        continue
      number = number + 1
      if number % 4 == 0:
        v = mass.index(element)
        mass[v] = 0
        print(mass)
        count = count + 1
      continue
  end = []
  for x in mass:
    if x!= 0:
      end.append(x)
  return end  

print(survive(n, k))
