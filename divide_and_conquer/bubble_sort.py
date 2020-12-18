arr=[23,4,5,1,22,34,345,2,325,463,1,24,6]
temp=0

def sort_bubble (arr, l=len(arr)):
  if l==1 or l==0:
    return arr
  else:
    for i in range(0,l-1):
      if arr[i]>arr[i+1]:
        temp=arr[i]
        arr[i]=arr[i+1]
        arr[i+1]=temp
    sort_bubble(arr, l-1)

sort_bubble(arr)

for i in range(len(arr)):
  print(arr[i])
     


