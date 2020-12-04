# Реализуйте алгоритм Евклида с помощью рекурсии

def euclidus(a, b):
    if (a == b):
        return a
    elif (a > b):
        return euclidus(a - b, b)
    elif (a < b):
        return euclidus(a, b - a)

print(euclidus(9, 5))