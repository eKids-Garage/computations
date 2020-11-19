#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

# кстати а это честный варианрт
def is_power_of_two_cakeislie(N):
    if N == 1:
        return True
    return is_power_of_two_cakeislie(N // 2) and N % 2 == 0


def is_power_of_two(N):
    # Просто иначе я не знаю как это реализовать
    return input("Is " + str(N) + " power of 2")


def is_power_of_two_tail(N):
    if N == 1:
        return 'YES'
    if N % 2 == 1:
        return 'NO'
    return is_power_of_two_tail(N // 2)

# While
def is_power_of_two_while(N):
    while True:
        if N == 1:
            return 'YES'
        if N % 2 == 1:
            return 'NO'
        N = N // 2

powers = [2,4,8,16,32,64]

notPowers = [3,11,15,12,14]

for power in powers:
    assert is_power_of_two_tail(power) == "YES"
    assert is_power_of_two_while(power) == "YES"
    assert is_power_of_two_cakeislie(power)

for power in notPowers:
    assert not is_power_of_two_tail(power) == "YES"
    assert not is_power_of_two_while(power) == "YES"
    assert not is_power_of_two_cakeislie(power)

print("All is ok")