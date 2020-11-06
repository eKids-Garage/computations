# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.

def prime_div(N, k = 2):
    if N % k == 0:
        print(k)
        prime_div(N // k, 2)
    elif k == N or N == 1:
        return
    else:
        prime_div(N, k + 1)


prime_div(2)
print("===")
prime_div(100)
print("===")
prime_div(2310)
print("===")