# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать цикл, а также строки, списки, массивы

def sum(N, res):
    res = res + N % 10
    N = N // 10
    if(N != 0):
      sum(N, res)
    else:
      print(res)

N = int(input("Print any number: "))
res = 0
sum(N, res)

