# Реализуйте сортировку слиянием (merge sort)
# Попытайтесь реализовать ее как при помощи обычной, 
# так и при помощи хвостовой рекурсии. Желательно, но необязательно
# реализовать оба варианта


def merge(left, right):
    result = []
    i = j = 0

    for k in range(0, len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
            if i == len(left):
                result.extend(right[j:])
                break
        else:
            result.append(right[j])
            j += 1
            if j == len(right):
                result.extend(left[i:])
                break
    
    return result

    

def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr

    left = arr[:n//2]
    right = arr[n//2:n]

    left = merge_sort(left)
    right = merge_sort(right)
    arr = merge(left, right)

    return arr

def merge_sort_tail(arr):
    return arr


print(merge_sort([6, 1, 5, 3]))

