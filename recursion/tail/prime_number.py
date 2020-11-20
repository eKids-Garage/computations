# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def is_prime(n):
  return("1")
#я не знаю как сделать обычную рекурсию:(
    
def is_prime_tail(n, k):
  if k <= n - n % 2:
    if n % k == 0:
      print("NO")
    else:
      is_prime_tail(n, k + 1)
  else:
    print("YES")

n = int(input("Number:"))
k = 2
is_prime_tail(n, k)

while k <= n - n % 2:
  if k == n - n % 2:
    if n % k == 0:
      print("NO")
      k = n + 1
    else:
      print("YES")
      k = k + 1
  else:
        if n % k == 0:
          print("NO")
          k = n + 1
        else:
          k = k + 1
