# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  

def prime_div(N, k):
      
    if N / k < k:
        print (str(N) + " | " + str(N) + " Всё!\n")
        return

    if (N % k == 0):
        print (str(N) + " | " + str(k))
        N = N // k
    else:
        k = k + 1
   
    prime_div(N, k)


prime_div(8235682364, 2)
prime_div(243, 2)
prime_div(850, 2)