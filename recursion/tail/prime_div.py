# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def dividors(N,k=2):
  if N/k<k:
    return [N]
  else:
    if N%k==0:
      return [k]+dividors(N//k,k)
    else:
      return dividors(N,k+1)



def dividors_tail(N, k=2):
  if N/k<k:
    print(N)
  else:
    if N%k==0:
      print(k)
      dividors_tail(N//k,k)
    else:
      dividors_tail(N,k+1)

#while
N=36
k=2
while k<=N:
    if N%k==0:
      print(k)
      N= N//k
    else:
      k+=1
print("\n")
#while

result=dividors(36)
for i in result:
  print(i)
print("\n")
dividors_tail(36)
