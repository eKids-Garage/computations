# Реализуйте алгоритм Евклида с помощью рекурсии

def euclidus(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b



a = int(input("число 1:"))
b = int( input("число 2:"))
print ("НОД:", euclidus(a,b))
