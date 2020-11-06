# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 

N = int(input())
c = 2
def prime(x,c):
  if x>3 and x % c != 0: 
    return prime(x,c+1)
  elif x>3 and x % c == 0 and c < x**(1/2):
    return "NO"
  else:
    return "YES"
print(prime(N,c))