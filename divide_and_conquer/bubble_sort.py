# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.

def sort_bubble(arr):
    for k in range(len(arr)-1):
        for i in range(len(arr)-k-1):
            if arr[i] > arr[i+1]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
    

    return arr
