# Реализуйте сортировку слиянием (merge sort)
# Попытайтесь реализовать ее как при помощи обычной, 
# так и при помощи хвостовой рекурсии. Желательно, но необязательно
# реализовать оба варианта 

def merge(one, two):
    Res = []
    i = 0
    j = 0
    while i < len(one) and j < len(two):
        if one[i] <= two[j]:
            Res.append(one[i]) 
            i += 1 
        else:
            Res.append(two[j]) 
            j += 1 
    Res += one[i:] + two[j:] 
    return Res


def merge_sort(arr): 
    if len(arr) <= 1: 
        return arr 
    else:
        L = arr[:len(arr) // 2] 
        R = arr[len(arr) // 2:] 
    return merge(merge_sort(L), merge_sort(R))

list = [1, 5, 244, 16, 71, 451, 7, 4]
print(merge_sort(list))
