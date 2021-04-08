# Реализуйте алгоритм Евклида с помощью рекурсии

def euclidus(a, b):
  if a%b==0:
    print(b)
  else:
    if b%a==0:
      print (a)
    elif a>b:
     euclidus(b, a%b)
    else:
     euclidus(a, b%a)

euclidus(6, 18)


    