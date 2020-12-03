# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.
#def sort_bubble(arr):




lst = [5,8,0,2,6,10,4,9,7,1,3]
count = len(lst) - 1
while count != 0:
  j = 0 
  while j < count:
    if lst[j] > lst[j + 1]:
      lst[j], lst[j + 1] = lst[j + 1], lst[j]
    j += 1  
  count -= 1

print(lst)      

