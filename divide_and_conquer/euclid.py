# Реализуйте алгоритм Евклида с помощью рекурсии

def euclidus(a, b):
  if a != b and  a%b!= 0:
    c = b
    b = a%b
    a = c
    euclidus(a, b)
    return b
    
  else:
    return min(a, b)
  

    

print(euclidus(8, 7))