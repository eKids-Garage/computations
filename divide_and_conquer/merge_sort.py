# Реализуйте сортировку слиянием (merge sort)
# Попытайтесь реализовать ее как при помощи обычной,
# так и при помощи хвостовой рекурсии. Желательно, но необязательно
# реализовать оба варианта

import random

def merge_sort(arr):
    # print(arr)
    if len(arr) <= 1:
        return arr
    elif len(arr) == 2:
        if arr[0] < arr[1]:
            return arr
        else:
            return arr[::-1]

    oe = arr[len(arr) // 2]
    L = []
    R = []
    for el in arr[:len(arr) // 2]:
        if el <= oe:
            L.append(el)
        else:
            R.append(el)

    for el in arr[(len(arr) // 2) + 1:]:
        if el <= oe:
            L.append(el)
        else:
            R.append(el)

    return merge_sort(L) + [oe] + merge_sort(R)

def merge_sort_tail(arr):
    return arr

def t(arr):
    random.shuffle(arr)
    return arr

print(merge_sort(t([1,2,5])))
print(merge_sort(t([1,2,5,4,8,7,9])))
print(merge_sort(t([1,2,5,6,6,6,4,5])))