# Реализуйте сортировку слиянием (merge sort)
# Попытайтесь реализовать ее как при помощи обычной, 
# так и при помощи хвостовой рекурсии. Желательно, но необязательно
# реализовать оба варианта

def merge_sort (inp):
  if len(inp) == 1:
    return inp
  else:
    L = merge_sort(inp[:len(inp) // 2])
    R = merge_sort(inp[len(inp) // 2:])
  return merge(L, R)

  return merge(L,R)

def merge(L,R):
  result = []
  l1 = 0
  r1 = 0
  while l1 < len(L) and r1 < len(R):
    if L[l1] < R[r1]:
      result.append(L[l1])
      l1+=1
    else:
      result.append(R[r1])
      r1+=1
  if r1 < len(R):
    result += R[r1:]
  if l1 < len(L):
    result += L[l1:]
  return result


print(merge_sort([2,1,4,3,8,7,5]))