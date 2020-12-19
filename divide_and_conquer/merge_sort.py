def merge_sort(arr):
  i=0
  j=0
  l=len(arr)
  if l>1:
    Left=arr[:l//2]
    Right=arr[-l//2:]
    merge_sort(Left)
    merge_sort(Right)
    for k in range(0, l):
      if len(Left)>i:
        if len(Right)>j:
          if Left[i]<=Right[j]:
            arr[k]=Left[i]
            i=i+1
          else:
            arr[k]=Right[j]
            j=j+1
        else:
          arr[k]=Left[i]
          i=i+1
      else: 
        arr[k]=Right[j]
        j=j+1
  else:
    return(arr)
  
  
list=[6,5,4,3,2,45,7,88,9,1,1,1,1,4,-3]
merge_sort(list)

print(list)