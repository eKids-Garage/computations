# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.

def sort_bubble (arr):
  for j in range(len(arr) - 1, 0, -1):
    for i in range(0, j):
      if arr[i] > arr[i + 1]:                                 
        temp = arr[i + 1]
        arr[i + 1] = arr[i]
        arr[i] = temp
  return arr

print(sort_bubble([1]))
print(sort_bubble([2, 1]))
print(sort_bubble([3, 2, 1]))
print(sort_bubble([5, 4, 3, 2, 1]))

