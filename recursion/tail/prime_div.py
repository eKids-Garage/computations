# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while
N = int(input("Введите число: "))

#def prime_div1(N, k):
#не знаю как сделать обычную рекурсию


def prime_div2(N, k):
  if N == 1:
    return 1 
  else:
    if N % k == 0:
      print (k)
      N = N // k
      return prime_div2(N, k)
    else:
      k += 1
      return prime_div2(N, k)   

def while_prime_div(N, k):
  while N == 1:
    return 1 
  else:
    if N % k == 0:
      print (k)
      N = N // k
      return while_prime_div(N, k)
    else:
      k += 1
      return while_prime_div(N, k)   

#print ("Обычный вариант:")
#print (prime_div1(N))  
print ("Хвостовой вариант:")
print (prime_div2(N, 2))  
print ("While вариант:")
print (while_prime_div(N, 2))  