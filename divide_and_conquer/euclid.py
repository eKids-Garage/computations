# Реализуйте алгоритм Евклида с помощью рекурсии

def euclidus(a, b):
  if a%b==0:
    print(b)
  else:
    if a>b:
     euclidus(b, a%b)
    else:
     euclidus(a, b%a)

euclidus(9823461, 2345673345)

    