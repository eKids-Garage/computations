# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 

N = int(input("Введите число:"))
def is_prime(N, c = 2):
  
  if c > N**0.5:
    return "YES"
  if N % c == 0:
    return "NO"
  return is_prime(N, c + 1)


print(is_prime(N))


def is_prime_tail(N, c = 2):
  while c <= N**0.5 :
    if N % c == 0:
      return "NO"
    return is_prime(N, c + 1)
  return "YES"
print(is_prime_tail(N))