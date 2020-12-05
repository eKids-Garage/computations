def bubble_sort(arr):

  for rangeForIter in range(len(arr)-1, 1, -1):
    for iter in range(rangeForIter):
      if arr[iter] > arr[iter+1]:
        arr[iter], arr[iter+1] = arr[iter+1], arr[iter]

  print (arr)

