# Реализуйте алгоритм Евклида с помощью рекурсии

def euclidus(a, b):
  if a != b:
    if a > b:
      a -= b
    else:
      b -= a
  else:
    print(b)  
    quit()    
  euclidus(a,b)    
euclidus(400,600)   