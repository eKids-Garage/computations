# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while
N = int(input("Введите число для проверки на простоту: "))
c=2

def is_prime(N):
  global c
  if N == 2:
    return "YES"
  elif c > N/2:
     return "YES"
  elif N % c == 0:
    return "NO"
  else:
    c += 1
    return is_prime(N)

    
def is_prime_tail(n, k):
  if N == 2:
    return "YES"
  elif k > N/2:
     return "YES"
  elif N % k == 0:
    return "NO"
  else:
    return is_prime_tail(N, k + 1)

def is_prime_while(n, k):
  while  N!=2:
    if k > N/2:
      return "YES"
    elif N % k == 0:
      return "NO"
    else:
      return is_prime_while(N, k + 1)
    return "YES"



print ("Обычная " , is_prime(N))
print("Хвостовая " , is_prime_tail(N, 2)) 
print("While " , is_prime_while(N, 2)) 

