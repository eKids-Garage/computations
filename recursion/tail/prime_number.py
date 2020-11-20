# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
# Оформите в виде обычной и хвостовой рекурсии


# вариант с циклом while
def divide_by_c_cycle(N, c):

    while c != N ** 1/2:

        if N % c == 0:
            print(str(N) + " делится без остатка на " + str(c))
            return "NO"

        return "YES"   


# вариант с хвостовой рекурсией
def divide_by_c_tail(N, c):

    if N % c == 0:
        print(str(N) + " делится без остатка на " + str(c))
        return "NO"

    if (c > N ** 0.5):
        return "YES"
    
    return divide_by_c_tail(N, c + 1)


def is_prime(N):
    return divide_by_c_cycle(N, 2) 


def is_prime_tail(N):  
    return divide_by_c_tail(N, 2)


print(is_prime(1231))
print(is_prime_tail(1231))