# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

N = int(input())
def prime(x,c):
   if c >= x:
     return "YES"
   if x%c!=0 and prime(x,c+1) == "YES":
     return "YES"
   else:
     return "NO"
print(prime(N,2))



def prime_tail(x,c):
  if x>3 and x % c != 0: 
    return prime(x,c+1)
  elif x>3 and x % c == 0 and c < x**(1/2):
    return "NO"
  else:
    return "YES"
print(prime_tail(N,2)) 



def prime_while(x,c):
    if x < 3:
        return "YES"
    while c < x**(1/2):
        if x % c == 0:
            return "NO"
        else:
            c +=1 
    return "YES"
print(prime_while(N,2))