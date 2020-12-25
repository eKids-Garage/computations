# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его 53421
# как итеративно (используя цикл), так и рекурсивно.

arr = input ("Введите строку для сортировки: ")
ar = []
for i in arr:
  ar.append(i)

def bubble(arr):
  i =  0
  for c in range(1,len(arr)):
    while i != len(arr) - 1:
      if arr[i] > arr[i+1]:
        c = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = c
        bubble(arr)
      else:
          i = i + 1
  return arr

print (bubble(ar))