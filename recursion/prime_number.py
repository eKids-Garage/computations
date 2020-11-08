# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
N = int(input("Введите число:"))

def is_prime(n, c = 2):
  if c > int(n**0.5) :
    return "YES"
  if n % c == 0:
    return "NO" 
  return is_prime(n, c + 1)

print(is_prime(N))