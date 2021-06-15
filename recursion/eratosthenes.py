def sieve(c, p):
  global A
  if c < len(A):
    i = p-1
    while i < len(A):
      if (i+2) % p == 0:
        A[i] = False
      i += 1
    
    j = p - 1  
    while j < len(A):
      if A[j] == True:
        p = j+2
        break
      j += 1
    sieve(c+1, p)

#Задаем верхнюю и нижнюю границы
n = int(input("Input n: "))
m = int(input("Input m: "))

p = 2
A = []
i = 0
while i <= m-p:
  A.append(True)
  i += 1



c = 0
sieve(c, p)

#Выводим только подходящие простые числа
while c < len(A):
  if A[c] == True and (c+2)>=n:
    print(c+2)
  c += 1
