# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 


def is_prime (N, c):
  if N % c == 0:
    return "NO"
  else:
    if c < N - 1:
      c += 1
      return is_prime(N, c)
    else:
      return "YES"

print(is_prime(29, 2))
