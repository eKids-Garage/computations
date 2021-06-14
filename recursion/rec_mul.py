# Реализуйте алгоритм рекурсивного умножения. 
# Попробуйте реализовать его для чисел любого размера, 
# но также можно ограничиться числами с размерностью 
# степень двойки: 2, 4, 8, 16 и т.д.

def rec_mult(x, y, n, m):
  if n == 1:
        return (x * y)/m 
  else: 
        a = x // 10 ** (n // 2)
        b = x % 10 ** (n // 2)
        c = y // 10 ** (n // 2)
        d = y % 10 ** (n // 2)

        return (10**n * rec_mult(a, c, n//2, m) + 10**(n//2) * ((rec_mult(a, d, n//2, m) + rec_mult(b, c, n//2, m))) + rec_mult(b, d, n//2, m))


def karatsuba(a,b):
    q = w = 10
    n = k = o = m = l = 1
    while a // q > 0:
        q = q*10
        n = n + 1
    while b // w > 0:
        w = w*10
        k = k + 1    
    if k < n:
        o = 10 ** (n - k)
        b = b * o
        l = n
    if k > n:
        m = 10 ** (k - n)
        a = a * m 
        l = k 
    if m != o:
       m = m * o 
    if l % 2 > 0:
       a = a * 10
       b = b * 10
       l = l + 1
       m = m * 100   
    return rec_mult(a, b, l, m)



print(karatsuba(1234, 5678))





