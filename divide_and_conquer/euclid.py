def euclid(a, b):
  while (a != 0 and b != 0):
    if(a < b):
      a, b = b, a
    if (a % b == 0):
      return (b)
    else:
      a = a % b
  return (1) 
