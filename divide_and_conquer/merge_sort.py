from random import randint
N = randint(2,10)
arr = [randint(-10,10) for i in range(N)]
print(arr)

def merge_sort(arr):
  if len(arr) < 2:
    return(arr)
  else:
    L = merge_sort(arr[:len(arr)//2])
    R = merge_sort(arr[len(arr)//2:])
    return mergeLR(L, R)


def mergeLR(L, R):
  result = []
  i = 0
  j = 0
  while i < len(L) and j < len(R):
    if L[i] < R[j]:
      result.append(L[i])
      i += 1
    else:
      result.append(R[j])
      j += 1
  while i < len(L):
    result.append(L[i])
    i+=1
  while j < len(R):
    result.append(R[j])
    j+=1
  return result
  
print(merge_sort(arr))