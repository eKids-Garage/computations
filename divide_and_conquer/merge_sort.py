def merge(arr1, arr2):
  Arr = [ ]
  ind1 = 0
  ind2 = 0

  while (ind1 < len(arr1)) and (ind2 < len(arr2)):
    if arr1[ind1] < arr2[ind2]:
      Arr.append(arr1[ind1])
      ind1 += 1
    else:
      Arr.append(arr2[ind2])
      ind2 += 1

  while (ind1 < len(arr1)):
    Arr.append(arr1[ind1])
    ind1 += 1

  while (ind2 < len(arr2)):
    Arr.append(arr2[ind2])
    ind2 += 1
  return Arr

def merge_sort(a):
  part1 = a[:len(a)//2]
  part2 = a[len(a)//2:]

  if (len(part1) > 2):
    part1 = merge_sort(part1)
  else:
    if(len(part1) == 2):
      if (part1[0] > part1[1]):
        part1[1], part1[0] = part1[0], part1[1]
   
  if (len(part2) > 2):
    part2 = merge_sort(part2)
  else:
    if(len(part2) == 2):
      if (part2[0] > part2[1]):
        part2[1], part2[0] = part2[0], part2[1]

  res = merge(part1, part2)
  return res

  a = merge_sort(a)
  return a
