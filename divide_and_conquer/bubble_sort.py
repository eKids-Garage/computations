# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.
arr = [567, 567890, 234, 6, 5]
def sort_bubble(arr):
  for j in range(1, len(arr)):
    for i in range(0, len(arr) - j):
      if arr[i] > arr[i+1]:
        temp = arr[i+1]
        arr[i+1] = arr[i]
        arr[i] = temp
  return arr

print(sort_bubble(arr))

  





