# Реализуйте алгоритм Евклида с помощью рекурсии

def euclidusWhile(m, n):
  while m != n:
    if(m > n):
      m = m - n
    if(n > m):
      n = n - m
  return m

def euclidus(m, n):
  if (m > n):
    m = m - n
    return euclidus(m, n)
  if (m < n):
    n = n - m
    return euclidus(m, n)
  if (m == n):
    return m

m = int(input("Input m: "))
n = int(input("Input n: "))
print("Greatest Common Factor (using Recursion) is: ")
print(euclidus(m, n))
print("Greatest Common Factor (using While) is: ")
print(euclidusWhile(m, n))
