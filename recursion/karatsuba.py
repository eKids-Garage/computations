def rec_mult(x, y, n):
    if n == 1:
        print("n = 1: x = {0}, y = {1}".format(x, y))
        return x*y
    else:
        a = x // 10**(n//2)
        b = x % 10**(n//2)
        c = y // 10**(n//2)
        d = y % 10**(n//2)

        print("n = {4}: a = {0}, b = {1}, c = {2}, d = {3}".format(a, b, c, d, n))
        ac = rec_mult(a, c, n//2)
        bd = rec_mult(b, d, n//2)
        abcd = rec_mult(a+b, c+d, n//2)
        return 10**n * ac + 10**(n//2) * (abcd - ac - bd) + bd

def getLen(a):
    an = 1
    ann = 1
    while a >= ann:
        an += 1
        ann *= 10
    return an - 1


def karatsuba(a, b):
    an = getLen(a)
    bn = getLen(b)
    return rec_mult(a,b,max(an, bn))

print(karatsuba(121, 7788)) # 7788 - позвони и мы подбросим (оно само)
