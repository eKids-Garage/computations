def merge_sort(arr):
  if len(arr) == 1:
    return arr
  l_a = arr[:len(arr) // 2]
  r_a = arr[len(arr) // 2:]
  
  L = merge_sort(l_a)
  R = merge_sort(r_a)

  i = 0
  j = 0
  k = 0
  res = []
  for k in range(0,len(arr)):
    if i == len(L):
      while j < len(R):
        res.append(R[j])
        j += 1
      break
    if j == len(R):
      while i < len(L):
        res.append(L[i])
        i += 1
      break

    if L[i] < R[j]:
      res.append(L[i])
      i += 1
    else:
      res.append(R[j])
      j = j + 1
  return res



r = [6, 5, 4]
print(merge_sort(r))