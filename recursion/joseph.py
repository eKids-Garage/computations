
# i это индекс элементов в массиве 
# n это элемент который убьет следующего не нулевого
# '-1' - значит все готово

def find_next_alive(array, n):
    if  len(array) < 2 :
        print('Little array')
        return -1
    else:
        i = n + 1
        if n == len(array) -1:
            i = 0 
        while array[i] == 0: 
            if i == len(array) -1:
                i = -1
            i = i + 1 # получится 0 (что нам и нужно)
        if n == i:
            return -1
        else:   
            return i    


def kill(array, n, i):
    i = i + 1
    next = find_next_alive(array,n)# тот кто умрет
    if next == -1:
        return array #'Stop'
    array[next] = 0
    killer = find_next_alive(array,n) # тот кто потом убьет
    if killer == (-1):
        return 'Stop'
    else:
        return kill(array, killer,i)

''' Oбьявляем переменные , запускаем функции '''
array = []
number = int(input("Введите кол-во воинов : ")) 
for a in range (1,number + 1):
    array.append(a)
print('----', array)
n = 0
kill(array, n,0)

# преобразуем во множество чтоб убрать нули
res = set(array)
res.remove(0)
print('survive ',*res) # 'сам элемент
