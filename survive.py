people=[]
def survive(n,k):
  person=0
  while person<n:
    person=person+1
    people.append(person)
  x=0 
  round=0 
  while round<n-1:
    x=x+k-1
    if x>n-round:
      x=x-n
    round += 1 
    people.pop(x)
  return people  

print(survive(16,2))
   