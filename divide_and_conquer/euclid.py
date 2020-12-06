# Реализуйте алгоритм Евклида с помощью рекурсии
a = int(input())
b = int(input())
def euclid(x, y):
    while x != y:
        if x > y:
            x-= y
        else:
            y -= x        
    print(a)
euclid(a,b)