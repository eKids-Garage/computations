# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.

def sort_bubble(inp, k=0):
  if len(inp) == 0:
    return []
  for i in range(len(inp)-1-k):
    if inp[i]>inp[i+1]:
      inp[i+1], inp[i] = inp[i], inp[i+1]
  if k == len(inp)-1:
    return inp 
  return sort_bubble(inp, k+1)    
print(sort_bubble([7,10,8,9,1,5,6,2,3,4]))
