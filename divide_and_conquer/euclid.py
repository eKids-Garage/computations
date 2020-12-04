# Реализуйте алгоритм Евклида с помощью рекурсии

def euclidus(a, b):
    r = a % b
    if r == 0:
        return b
    return euclidus(b, r)

print(euclidus(90, 60))