import math

def rec_mult(x, y, n):
    if n == 1:
        #print("n = 1: x = {0}, y = {1}".format(x, y))
        return x*y
    else: 
        a = x // 10**(n//2)
        b = x % 10**(n//2)
        c = y // 10**(n//2)
        d = y % 10**(n//2)

        #print("n = {4}: a = {0}, b = {1}, c = {2}, d = {3}".format(a, b, c, d, n))

        return 10**n * rec_mult(a, c, n//2) + 10**(n//2) * (rec_mult(a, d, n//2) + rec_mult(b, c, n//2)) + rec_mult(b, d, n//2)

def karatsuba(x, y):

    # найти максимальную длину
    lx = int(len(str(x)))
    ly = int(len(str(y)))
    
    maxLen = max(lx, ly)
  
    # определить ближайшую разрядность, равную степени двойки - D
    d = int(math.ceil(math.log(maxLen, 2)))
    D = 2 ** d

    # "добить" x и y нолями до разрядности D
    # запомнить сколько нолей добавили к x и y
    dx = D - lx
    dy = D - ly
    x = x * (10 ** dx)
    y = y * (10 ** dy)

    #print("maxLen = {0}, d = {1}, D = {2}, x = {3}, y = {4}".format(maxLen, d, D, x, y))

    # потом запустить нашу карацубу для степеней двойки
    # убрать лишние ноли
    return rec_mult(x, y, D) // (10 ** (dx + dy))

a = 87651
b = 5432
print(karatsuba(a, b))
print(a * b)