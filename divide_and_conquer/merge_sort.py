# Реализуйте сортировку слиянием (merge sort)
# Попытайтесь реализовать ее как при помощи обычной, 
# так и при помощи хвостовой рекурсии. Желательно, но необязательно
# реализовать оба варианта 

def merge(arr, Arr):
    Res = []
    i = 0
    j = 0
    while i < len(arr) and j < len(Arr):
        if arr[i] <= Arr[j]:
            Res.append(arr[i]) 
            i += 1 
        else:
            Res.append(Arr[j]) 
            j += 1 
    Res += arr[i:] + Arr[j:] 
    return Res


def merge_sort(arr): 
    if len(arr) <= 1: 
        return arr 
    else:
        L = arr[:len(arr) // 2] 
        R = arr[len(arr) // 2:] 
    return merge(merge_sort(L), merge_sort(R))

list = [1, 5, 244, 15, 61, 176, 8, 4]
print(merge_sort(list))

