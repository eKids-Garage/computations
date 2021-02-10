# Реши задачу Иосифа Флавия:
# где n - число солдат, k - шаг (2 - каждый второй (сосед), 3 - каждый третий и т.д.)
# 
# 1. survive(n, k) - используя массив. 
# 2. survive_num(n, k) - без использования массива 

def survive(n, k):
    
    # создаём массив, значение элемента равно индексу, начало с 0
    arr = []
    for i in range(0, n):
        arr.append(i)
    #print(arr)

    k = k - 1 # если каждый третий, то убиваем через 2
    next_kill = 0

    while (len(arr) > k):
        next_kill += k

        # если массив закончился, то переходит на начало
        if (next_kill >= len(arr)):
            next_kill = next_kill - len(arr)
        
        # удаляем из массива, размер станет меньше на 1
        del arr[next_kill]
        #print(arr)
    
    return arr

print(survive(41, 2))