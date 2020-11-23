# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while


# вариант с циклом while
def dividors(N):
    
    k = 2
    
    while (N / k >= k):
        if (N % k == 0):
            print (str(N) + " | " + str(k))
            N = N // k
        else:
            k = k + 1
    
    print (str(N) + " | " + str(N) + " Всё!\n")


# хвостовая рекурсия
def dividors_tail(N, k):
      
    if N / k < k:
        print (str(N) + " | " + str(N) + " Всё!\n")
        return

    if (N % k == 0):
        print (str(N) + " | " + str(k))
        N = N // k
    else:
        k = k + 1
   
    dividors_tail(N, k)


dividors(8235682364)
dividors(243)
dividors(850)
dividors_tail(8235682364, 2)
dividors_tail(243, 2)
dividors_tail(850, 2)