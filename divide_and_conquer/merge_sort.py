# Реализуйте сортировку слиянием (merge sort)
# Попытайтесь реализовать ее как при помощи обычной, 
# так и при помощи хвостовой рекурсии. Желательно, но необязательно
# реализовать оба варианта

def merge_sort(A):
  if len(A) == 1:
    return A
  if len(A) == 2:
    if A[0] > A[1]:
      A[0], A[1] = A[1], A[0]
    return A
  K = len(A) // 2
  B = A[:K]
  C = A[K:]
  B = merge_sort(B)
  C = merge_sort(C)
  i = 0
  j = 0
  l = 0
  while i < len(B) and j < len(C):
    if B[i] < C[j]:
      A[l] = B[i]
      i = i + 1
    else:
      A[l] = C[j]    
      j = j + 1
    l = l + 1
  while i < len(B):
    A[l] = B[i]
    i = i + 1
    l = l + 1
  while j < len(C):
    A[l] = C[j]
    j = j + 1
    l = l + 1      
  return A
print(merge_sort([5,3,1,4,2]))




