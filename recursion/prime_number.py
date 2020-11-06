# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
import math
def is_prime(N,d=2):
  if (d>math.sqrt(N)):
    print('prime')
  elif (N==N//d*d):
     print('non prime')
  else :
    is_prime(N,d=d+1)
num=input()
num=int(num)
is_prime(num)