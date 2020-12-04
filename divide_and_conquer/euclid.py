
def euclid(a, b):
  if(a == b):
    return a
  if(a > b):
    return euclid(a - b, b)
  if (a < b):
    return euclid(a, b - a)


a = int(input())
b = int(input())
print (euclid(a, b))