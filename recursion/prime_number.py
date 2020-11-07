# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
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

print (is_prime(N))