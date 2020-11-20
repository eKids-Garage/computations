# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи в функциях sum и sum_tail нельзя использовать цикл, а также строки, списки, массивы
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def sum(N):
  if N>=10:
    return N % 10 +sum(N//10)
  else:
    return N

def sum_tail(N, s=0):
  if N>=10:
    return sum_tail(N//10, s+N % 10)
  else:
    return s+N % 10

#while
N=21348
s=0
while N>=10:
  s+=N%10
  N=N//10
print(s+N)
#while

print(sum_tail(21348))
print(sum(21348))