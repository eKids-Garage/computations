# Реализуйте алгоритм Евклида с помощью рекурсии

def euclidus(a, b):
  if a == b:
    return(a)
  elif a > b:
    return euclidus(a - b, b)
  else:
    return euclidus(a, b - a)