# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.

def bubble(arr, i):
  while i != len(arr) - 1:
    if arr[i] > arr[i + 1]:
      a = arr[i]
      arr[i] = arr[i + 1]
      arr[i + 1] = a
    else:
      if arr[i] < arr[i + 1]:
        i = i + 1
      else:
        if arr[i] == arr[i + 1]:
          i = i + 1

i = 0
arr = [5, 4, 3, 2, 1]
d = 1

while d < len(arr):
  bubble(arr, i)
  d = d + 1

for a in arr:
  print(a)

