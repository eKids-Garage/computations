# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  

def prime_div(N, k):
    if N > 1:
        if N % k == 0:
            print(k)
            N /= k
            prime_div(N, k)
        else:
            prime_div(N, k + 1)

print(prime_div(210, 2))