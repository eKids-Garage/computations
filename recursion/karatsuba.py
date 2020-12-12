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

        return 10**n * rec_mult(a, c, n//2) + 10**(n//2) * (rec_mult(a, d, n//2) + rec_mult(b, c, n//2)) + rec_mult(b, d, n//2)

print(rec_mult(9656, 8578, 4))
