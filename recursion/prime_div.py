# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  

def prime_div(N, k):

    if N%k==0 and N/k==1:
        print (k)

    elif N%k==0:
        print(k)
        return prime_div(N/k, 2)
    else:
        return prime_div(N, k+1)