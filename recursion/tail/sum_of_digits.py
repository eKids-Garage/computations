# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи в функциях sum и sum_tail нельзя использовать цикл, а также строки, списки, массивы
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def sum(N):
    if N == 0:
        return 0

    return sum(N//10) + N % 10


def sum_tail(N, s=0):
    if N == 0:
        return s

    return sum_tail(N // 10, s + N % 10)

def sum_while(N):
    s = 0
    while True:
        if N == 0:
            return s
        s += N % 10
        N = N // 10

print(sum(123))
print(sum(456))
print(sum_tail(123))
print(sum_tail(456))
print(sum_while(123))
print(sum_while(456))