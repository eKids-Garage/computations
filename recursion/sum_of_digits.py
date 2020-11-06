# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать цикл, а также строки, списки, массивы
N = int(input("введите натуральное число "))
summ = 0
def sum(N,summ):
  if N < 1:
    return summ
  summ = summ + N % 10
  N = N//10
  return sum(N,summ)
print(sum(N,summ))

