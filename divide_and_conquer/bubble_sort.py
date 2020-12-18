# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.
y=0
x=0
def sort_bubble (arr):
  r=len(arr)
  global x
  global y
  while r>=x:
    if arr[y]>arr[y+1]:
      z=arr[y]
      arr[y]=arr[y+1]
      arr[y+1]=z
    if r-2==y:
      x=x+1
      y=0
    else:
      y=y+1   
  return(arr)          
  

arr=[3,5,4,2,1]
print(sort_bubble(arr))