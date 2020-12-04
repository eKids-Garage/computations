# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.

def sort_bubble (arr):
    pos = 0
    unsorted = len(arr) - 1
    while unsorted > 0:
        while pos < unsorted:
            if arr[pos+1] < arr[pos]:
                t = arr[pos]
                arr[pos] = arr[pos+1]
                arr[pos+1] = t
            pos += 1
        pos = 0
        unsorted -= 1
    return arr

print(sort_bubble([1,5,8,4,1,2]))