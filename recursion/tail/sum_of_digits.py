# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи в функциях sum и sum_tail нельзя использовать цикл, а также строки, списки, массивы
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while
def sum(N):
  res = N % 10
  N = N // 10
  if N == 0:
    return res
  else:
    return res + sum(N)

def sum_tail(N, res):
  res = res + N % 10 
  N = N // 10
  if N == 0:
    return res
  else: 
    return sum_tail(N, res)

def sum_while(N):
  res = 0
  while N != 0:
    res = res + N % 10
    N = N // 10
  return res

N = int(input("Input any number: "))
res = 0
print(sum(N))
print(sum_tail(N, res)) 
print(sum_while(N))

