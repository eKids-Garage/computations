# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.

a = [5, 7, 4, 2, 6, 8, 0]

def sort_bubble(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j + 1] < arr[j]:
              x = arr[j]
              arr[j] = arr[j + 1]
              arr[j + 1] = x
    return arr

print(a)
print(sort_bubble(a))