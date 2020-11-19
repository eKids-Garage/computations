# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

# Я знаю что оно странное, но оно работает
def dividors(N, k=-1):
    if k == -1:
        k = N - 1

    if k <= 1:
        return False, N

    suc, newN = dividors(N, k - 1)
    if not suc:
        if N % k == 0:
            print(k)
            return True, N // k
        else:
            return False, N

    suc, N2 = dividors(newN)
    return True, N2

def dividors_tail(N, k=2):
    if N == 1:
        return

    if N == k:
        print(k)
        return

    if N % k == 0:
        print(k)
        dividors_tail(N // k)
    else:
        dividors_tail(N, k + 1)


def dividers_while(N):
    k = 2
    while True:
        if N == 1:
            return

        if N == k:
            print(k)
            return

        if N % k == 0:
            print(k)
            N = N // k
        else:
            k = k + 1

print(dividors(2*3*5*11)[1])
print()
dividors_tail(2 * 3 * 5 * 11)
print()
dividers_while(2*3*5*11)
