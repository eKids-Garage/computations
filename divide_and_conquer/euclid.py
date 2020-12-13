# Реализуйте алгоритм Евклида с помощью рекурсии

def euclidus(a, b):
  if(a != 0 and b != 0):
    if (a != b):
      while(a != b):
          if a > b:
              a = a - b
          else:
            b = b - a
      return(a)
    else:
      return(a)
  else:
    return(a + b)
a = int(input())
b = int(input())
print(euclidus(a, b))