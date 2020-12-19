# Реализуйте сортировку слиянием (merge sort)
# Попытайтесь реализовать ее как при помощи обычной, 
# так и при помощи хвостовой рекурсии. Желательно, но необязательно
# реализовать оба варианта

def merge_sort(arr):

    print(arr)
    if (len(arr) > 1):
        # разбиваем на 2 части - L and R
        m = len(arr) // 2
        L = arr[:m]
        R = arr[m:]
        # запускаем себя для каждой из частей
        merge_sort(L)
        merge_sort(R)
        # объединяем L и R в один сортированный массив
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # осталось добить остатки
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr

# ==========================
a = [9, 4, 5, 2, 4, 8, 1, 0, 3]
print (a)


print(merge_sort(a))

