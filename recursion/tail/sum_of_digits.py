# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи в функциях sum и sum_tail нельзя использовать цикл, а также строки, списки, массивы
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while
N = input("Type your number:")
N = int(N)
Sum = 0
digit = 0


#usual recursion(not tail)
def sum(N):
  if N <= 1:
      return N
  else:
      return N % 10 + sum(N//10)
    
print("\nSolving problem with help of usual recursion(not tail):")    
print(sum(N))    


#tail recursion
def sum_tail(N, Sum):
  if N >= 1:
    digit = N % 10
    Sum = Sum + digit
    N = N // 10
    return sum_tail(N, Sum)
  else:
    return Sum
      
print("\nWith help of tail recursion:")
print(sum_tail(N, Sum))


#while loop
while N >= 1:
  digit = N % 10
  Sum = Sum + digit
  N = N // 10
  
print("\nWith help of while loop:")  
print(Sum)  