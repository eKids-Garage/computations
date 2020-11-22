# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

N = int(input("Введите число:"))
def is_prime(N, k = 2):
  if k > N**0.5:
    return "YES"
  if N % k == 0:
    return "NO"
  return is_prime(N, k + 1)


print(is_prime(N))


def is_prime_tail(N, k = 2):
  while k <= N**0.5 :
    if N % k == 0:
      return "NO"
    return is_prime(N, k + 1)
  return "YES"

print(is_prime_tail(N))
