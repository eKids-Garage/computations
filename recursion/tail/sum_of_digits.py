# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи в функциях sum и sum_tail нельзя использовать цикл, а также строки, списки, массивы
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def sum(N):
  if N < 1:
    return N
  else: 
    return N % 10 + sum(N // 10)



def sum_tail(N, s):
  if N < 1:
    return s
  s = s + N % 10
  N = N//10
  return sum_tail(N,s)


def sum_tail_while(N, s):
  while N > 1:
    s = s + N % 10
    N = N//10
  return s
  
print(sum_tail_while(586721, 0))    
print(sum(586721))

print(sum_tail(586721, 0))



