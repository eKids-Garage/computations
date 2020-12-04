# Реализуйте алгоритм Евклида с помощью рекурсии

def euclidus(a, b):
    if max(a,b) % min(a,b) == 0:
        return min(a,b)
    return euclidus(min(a,b), max(a,b) % min(a,b))

print(euclidus(6*4, 6))
print(euclidus(6*4, 6*2))
print(euclidus(6*4, 6*3))
print(euclidus(2*5, 3*7))