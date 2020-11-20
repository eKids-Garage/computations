# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи в функциях sum и sum_tail нельзя использовать цикл, а также строки, списки, массивы
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def sum(n):
  if n != 0:
    return n % 10 + sum(n // 10)
  else:
    return(n)

def sum_tail(n, k):
  if n != 0:
    k = k + n % 10
    sum_tail(n // 10, k)
  else:
    print(k)    

n = int(input("Number:"))
k = 0
sum_tail(n, k)
print(sum(n))

while n != 0:
  k = k + n % 10
  n = n // 10

print(k)