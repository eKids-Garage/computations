# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи в функциях sum и sum_tail нельзя использовать цикл, а также строки, списки, массивы
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

N = int(input())

def SUM(x):
    if x // 10 != 0:
        return x % 10 + SUM(x//10)
    else:
        return x
print(SUM(N))
 
 
 
 
def SUM_tail(x, a):
  if x // 10 == 0:
    return a + x
  else:
    a += x % 10
    return SUM_tail(x // 10, a)
print(SUM_tail(N,0))




def SUM_while(x,a):
    a = 0
    while x >= 1:
        a += x%10
        x //= 10
    return(a)
print(SUM_while(N,0))