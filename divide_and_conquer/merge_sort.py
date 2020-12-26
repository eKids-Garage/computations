# Реализуйте сортировку слиянием (merge sort)
# Попытайтесь реализовать ее как при помощи обычной, 
# так и при помощи хвостовой рекурсии. Желательно, но необязательно
# реализовать оба варианта

def mergeSort(arr):
  if len(arr)>1:
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        arr[k] = left[i]
        i = i + 1
      else:
        arr[k] = right[j]
        j = j + 1
      k = k + 1

    while i < len(left):
      arr[k] = left[i]
      i = i + 1
      k = k + 1

    while j < len(right):
      arr[k] = right[j]
      j = j + 1
      k = k + 1

arr = [54,26,93,17,77,31,44,55,20,1]
print(arr)
mergeSort(arr)
print(arr)