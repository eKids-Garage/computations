import random 

length = random.randint(7,777) #  кол-во элементов генерируется
array = []
for i in  range (0 , length) : # для всех элементов в списке
  array.append(random.randint(7,777))   # генерирует элементы массива и их туда добавляет
print("первоначальный массив:",*array,"--конец массива\n")

def merge_sort(array):
    if len(array) < 2:
        return array
    else:
        half = len(array) // 2
        R = merge_sort(array[half:])
        L = merge_sort(array[:half])
        return(merge_arrays(L,R))

def merge_arrays(L,R):
    result = []    
    i = n = 0 
    while len(L) > i  and len(R)> n  :
        if L[i] < R[n]:
            result.append(L[i])
            i = i+1
        else:
            result.append(R[n])
            n = n+1
    if i < len(L):
        result = result+(L[i:])
        return result
    if n <len(R):
        result = result+(R[n:])
        return result

print(merge_sort(array))
print('lenght was:',len(array))
   
