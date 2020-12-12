# Реализуйте алгоритм Евклида с помощью рекурсии

def euclid(m, n):
    if m == n:
        print(n)
    elif n > m:
        n -= m
        euclid(m, n)
    elif m > n:
        m -= n
        euclid(m, n)

def euclid_while(m, n):
    while m != n:
        if n > m:
            n -= m
        elif m > n:
            m -= n
    print(n)