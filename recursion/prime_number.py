# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
c=2
def is_prime(N):
  global c
  if N%c != 0 :
    return "YES"
  if N%c == 0:
    return "NO"
  #c+=1
  return is_prime(N)

print(is_prime(2))
print(is_prime(3))
print(is_prime(5))
print(is_prime(7))
print(is_prime(11))
print(is_prime(13))
print(is_prime(17))
print(is_prime(19))