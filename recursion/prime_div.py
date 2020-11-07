# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  
N = input("Type your number:")
N = int(N)
k = 2

def prime_div(N, k):
    
    if N * k != k:
        if N % k == 0:
            print(k)
            N = N // k
            prime_div(N, k)
        else:
            k = k + 1
            prime_div(N, k)
    else:
        exit(0)
        
print(prime_div(N, k))  