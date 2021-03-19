# Реализуйте алгоритм рекурсивного умножения. 
# Попробуйте реализовать его для чисел любого размера, 
# но также можно ограничиться числами с размерностью 
# степень двойки: 2, 4, 8, 16 и т.д.

#retrieving data
N = input("Type your first number(which is a power of two):")
M = input("Type your second number(which is a power of two too):")
n = len(N)
M = int(M)
N = int(N)

#main function
def rec_mul(N, M, n):
    
    if n == 1:
        return N * M
    else:
        #splitting numbers
        a = N // 10**(n//2)
        b = N % 10**(n//2)
        c = M // 10**(n//2)
        d = M % 10**(n//2)
        #main algorithm
        return 10**n * rec_mul(a, c, n//2) + 10**(n//2) * rec_mul(a, d, n//2) + 10**(n//2) * rec_mul(b, c, n//2) + rec_mul(b, d, n//2)

print("\n", N, " * ", M, " = ", rec_mul(N, M, n))