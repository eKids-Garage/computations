# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать цикл, а также строки, списки, массивы
summa=0
def sum(N):

  global summa
  digit = N % 10
  summa+=digit
  if N>=10:
    return sum(N//10)
  else:
    return summa

print(sum(748296))
