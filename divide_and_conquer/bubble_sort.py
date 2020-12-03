# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.

def sort_bubble(arr):
  count = len(arr) - 1
  while count != 0:
    j = 0 
    while j < count:
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
      j += 1  
    count -= 1

  print(arr)      

sort_bubble([5,8,0,2,6,10,4,9,7,1,3])