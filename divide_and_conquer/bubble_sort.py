# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.


def sort_bubble(arr):
    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

list = [54,256,93,17,7,31,494,55,20]
sort_bubble(list)
print(list)