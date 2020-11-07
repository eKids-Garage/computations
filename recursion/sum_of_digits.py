# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать цикл, а также строки, списки, массивы

def sum(N):
    return sum_of_digits(N) 


def sum_of_digits(N):
    if N < 10:
        return N
   
    return N % 10 + sum_of_digits(N // 10)


print (sum(9876543210))
