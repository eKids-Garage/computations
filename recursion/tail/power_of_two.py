#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def is_power_of_two(N):
  if N == 2 or N==1:
    return 'YES'
  if N < 1:
    return 'NO'
  res=is_power_of_two(N//2)
  if res == "YES" and  N % 2 == 0 or res==1:
    return "YES"
  else:
    return 'NO' 



def is_power_of_two_tail(N):
  if N==2 or N ==1:
    return 'YES'
  if N % 2 != 0:
    return 'NO' 
  return is_power_of_two_tail(N//2)  

#while
N = 2048
res="-"
while N>=1:
  if N==2 or N ==1:
    res = 'YES'
    break
  if N % 2 != 0:
    res = 'NO' 
    break
  N = N/2
print(res+"\n")  
#while

print(is_power_of_two(16))
print(is_power_of_two_tail(16))
