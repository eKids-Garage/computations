def merge_sort(arr):

  if len(arr) == 1:
    return arr
  L = merge_sort(arr[:len(arr)//2])
  R = merge_sort(arr[len(arr)//2:])

  o = 0
  a = 0
  i = 0
  result = []
  for o in range(0,len(arr)):
    if L[i] < R[a]:
      result.append(L[i])
      i+=1
    else:
      result.append(R[a])
      a+=1
    
    if i == len(L):
      while a < len(R):
        result.append(R[a])
        i += 1
      break
    if  a == len(R):
      while i < len(L):
        result.append(L[i])
        i += 1
      break

  return result



print(merge_sort([9,8,7,6,5,4,3,2,1]))