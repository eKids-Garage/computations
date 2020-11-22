# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def dividors(N):
  #не смог(((((
    return 0


def dividors_tail(N, k):
  if N // k >= k:
    if N % k == 0:
      print(k)
      N = N // k
    else: 
	    k = k + 1
    dividors_tail(N, k)
  else:
    print(N)


dividors_tail(51, 2)   


def dividors_tail_while(N, k):
  while N // k >= 1:
    if N % k == 0:
      print(k)

      N = N // k
    else:
      k += 1
 
print("..................................")
dividors_tail_while(51, 2)
