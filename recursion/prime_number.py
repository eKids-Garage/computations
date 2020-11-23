# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 

c=2
def is_prime(N):
 global c
 if N%c==0:
    print("No")
 else:
   if c>0.5*N:
     print("Yes")
   else:
     c += 1
     return is_prime(N)

is_prime(17)