# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать цикл, а также строки, списки, массивы
N = input("Type your number:")
N = int(N)
digit = 0
Sum = 0

def sum(N):
    
    global Sum
    
    if N >= 1:
        digit = N % 10
        Sum = Sum + digit
        N = N // 10
        return sum(N)
    else:
        return Sum
print(sum(N))