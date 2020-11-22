# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while
N = 56677654
def is_prime(n):
   #я не смог без дополнительного каунтера
   return("YES")

def is_prime_tail(n, k):
  if n % k == 0:
    return "NO"
  if k >= n**0.5:
    return "YES"
  return is_prime_tail(n, k + 1)

def is_prime_while(n):
  k = 2
  while k <= n**0.5:
    if n % k == 0:
      return "NO"
    k += 1

  return("YES")

print(is_prime_tail(N, 2))  

print(is_prime_while(N))  
  