# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.

def sort_bubble (arr):
  l = len(arr)
  a = 0
  b = 0
  for i in range(l - 1):
    for j in range(l - i - 1):
      if arr[j + 1] < arr[j]:
        a = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = a
  return arr
length = int(input("Введите длину массива "))
arr = [0] * length
for k in range(length):
  arr[k] = int(input())
sort_bubble(arr)
for k in range(length):
  print(arr[k])