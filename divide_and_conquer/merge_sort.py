# Реализуйте сортировку слиянием (merge sort)
# Попытайтесь реализовать ее как при помощи обычной, 
# так и при помощи хвостовой рекурсии. Желательно, но необязательно
# реализовать оба варианта
def merge_sort(inp):
  if len(inp) < 2:
    return inp
  L = merge_sort(inp[:len(inp)//2])
  R = merge_sort(inp[len(inp)//2:])
  return merge(L, R)

def merge(L, R):
  res = []
  i1 = 0
  i2 = 0
  while i1 < len(L) and i2 < len(R):
    if L[i1] < R[i2]:
      res.append(L[i1])
      i1+=1
    else:
      res.append(R[i2])
      i2+=1
  if i2 < len(R):
    res += R[i2:]
  if i1 < len(L):
    res += L[i1:]
  return res

print(merge_sort([4,7,1,9,2,3,6,5,8]))


