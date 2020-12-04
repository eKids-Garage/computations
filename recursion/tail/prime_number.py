# Дано натуральное число N>1. Проверьте, является ли оно простым.
# Программа должна вывести слово YES, если число простое и NO, если число составное.
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def is_prime(N, k=2):
    if k == N:
        return True
    isOk = is_prime(N, k + 1)
    return isOk and N % k != 0


def is_prime_tail(N, k = 2):
    if k == N:
        return True
    if N % k == 0:
        return False
    return is_prime(N, k + 1)


def is_prime_while(N):
    k = 2
    while True:
        if k == N:
            return True
        if N % k == 0:
            return False
        k = k + 1


powers = [3,5,11,13]

notPowers = [4,6,8,9]

for power in powers:
    assert is_prime(power)
    assert is_prime_tail(power)
    assert is_prime_while(power)
    # assert is_power_of_two_cakeislie(power)

for power in notPowers:

    assert not is_prime(power)
    assert not is_prime_tail(power)
    assert not is_prime_while(power)
    # assert not is_power_of_two_cakeislie(power)

print("All is ok")
