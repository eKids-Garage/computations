def sort_bubble (arr):
  length = len(arr) - 1
  while (length > 0):
    for i in range (length):
      if (arr[i] > arr[i+1]):
        t = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = t

    length -= 1

  return arr


length = int(input())
arr = []
for i in range(length):
  arr.append(int(input()))
print (arr)
print (sort_bubble(arr))