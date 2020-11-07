# Дано натуральное число N>1. Проверьте, является ли оно простым.
# Программа должна вывести слово YES, если число простое и NO, если число составное.

def is_prime(N):
    return divide_by_c(N, 2)

def divide_by_c(N, c):

    if N % c == 0:
        print(str(N) + " делится без остатка на " + str(c))
        return "NO"

    if (c == int(N**0.5)):
        return "YES"
    
    return divide_by_c(N, c + 1)

print(is_prime(1233))
