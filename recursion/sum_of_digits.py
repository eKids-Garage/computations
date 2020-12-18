# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать цикл, а также строки, списки, массивы
n=int(input())

def sum(N):
  summa = 0
  digit = 0
  while N>0:
    digit = N%10
    summa = summa+digit
    N = N//10
  print(summa)
    


sum(n)