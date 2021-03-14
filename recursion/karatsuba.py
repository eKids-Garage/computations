def karatsuba(x, y, n):
    if n == 1:
#        print("n = 1: x = {}, y = {}".format(x, y))
        return x*y
    else: 
        a = x // 10**(n//2)
        b = x % 10**(n//2)
        c = y // 10**(n//2)
        d = y % 10**(n//2)

#        print("n = {}: a = {}, b = {1}, c = {}, d = {}".format(n, a, b, c, d))

        return 10**n * rec_mult(a, c, n//2) + 10**(n//2) * (rec_mult(a, d, n//2) + rec_mult(b, c, n//2)) + rec_mult(b, d, n//2)
