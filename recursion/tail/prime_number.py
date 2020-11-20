# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def is_prime(N,c=2):
  if c>=N:
    return "YES"
  if is_prime(N,c+1) == "YES" and N%c!=0:
    return "YES"
  else:
    return "NO"



def is_prime_tail(N,c=2):
  if N%c != 0 and c==N-1:
    return "YES"
  if N%c == 0:
    return "NO"
  return is_prime_tail(N,c+1)

#while  
N=17
c=2
res="NO"
while c<N:
  if N%c != 0 and c==N-1:
    res= "YES"
  if N%c == 0:
    res="NO"
    break
  c+=1
print(res+"\n")
#while

print(is_prime(12))
print(is_prime(13)+"\n")

print(is_prime_tail(12))
print(is_prime_tail(13))