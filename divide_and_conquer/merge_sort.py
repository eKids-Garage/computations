# Реализуйте сортировку слиянием (merge sort)
# Попытайтесь реализовать ее как при помощи обычной, 
# так и при помощи хвостовой рекурсии. Желательно, но необязательно
# реализовать оба варианта
A = [5, 3, 4, 0, 7, 2, 1]
def merge_sort(arr):
  if len(arr) > 1:
    mid = len(arr)//2
    l = arr[:mid]
    r = arr[mid:]
    merge_sort(l)
    merge_sort(r)
    k = 0
    i = 0
    j = 0
    while i < len(l) and j < len(r):
      if l[i] < r[j]:
        arr[k] = l[i]
        i=i+1
      elif l[i] > r[j]:
        arr[k] = r[j]
        j=j+1
      else:
        arr[k]=r[j]
        j=j+1
      k=k+1
    while i<len(l):
      arr[k]=l[i]
      i=i+1
      k=k+1
    while j<len(r):
      arr[k]=r[j]
      j=j+1
      k=k+1
    return arr
  else:
    return arr

print(merge_sort(A))


def merge_sort_tail(arr):
    return arr

