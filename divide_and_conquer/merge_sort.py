# Реализуйте сортировку слиянием (merge sort)
# Попытайтесь реализовать ее как при помощи обычной, 
# так и при помощи хвостовой рекурсии. Желательно, но необязательно
# реализовать оба варианта


def merge_sort(arr):
  n = len(arr)
  i = 0
  j = 0
 
  if n == 1:
    return arr
  
  if n > 1:
    L=arr[:n//2]
    R=arr[n//2:]

    merge_sort(L)
    merge_sort(R)
    
    for k in range(0, n):
      if len(L) > i:
        if len(R) > j:
          if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
          
          else:
            arr[k] = R[j]
            j+=1
        
        else:
          arr[k] = L[i]
          i+=1
      
      else: 
        arr[k] = R[j]
        j+=1
  

A = [8, 23, 66, 0, 5, 2, 0, 1]
merge_sort(A)
print(A)

B = [8]
merge_sort(B)
print(B)





