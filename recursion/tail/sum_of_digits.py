# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи в функциях sum и sum_tail нельзя использовать цикл, а также строки, списки, массивы
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

N = int(input("Введите число:"))
def sum(N):
  if N < 10:
    return N
  digit = N % 10
  return sum(N//10) + digit

print(sum(N))

def sum_tail(N, s = 0):
    while N > 0:
      digit = N % 10
      s = s + digit
      return sum_tail(N // 10, s)
    return s

print(sum_tail(N))

