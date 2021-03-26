# Реализуйте алгоритм рекурсивного умножения. 
# Попробуйте реализовать его для чисел любого размера, 
# но также можно ограничиться числами с размерностью 
# степень двойки: 2, 4, 8, 16 и т.д.
def length(m):
  while m > 0:
    i = m % 10
    m = m / 10
    m = m + i
  return m
def rec_mul(a, b):

    if(length(a) == 1 or length(b) == 1):
      return a * b
    else:
      x = a // 10**(length(a)//2)
      y = a % 10**(length(a)//2)
      z = b // 10**(length(a)//2)
      e = b % 10**(length(a)//2)
      return (rec_mul(y, z) * 10 ** (b // 2)) +(rec_mul(x, z) * 10 ** ((a + b) // 2)) + (rec_mul(x, e) * 10 ** (a // 2)) + rec_mul(y, e)
a = int(input())
b = int(input())
print(rec_mul(a, b))
