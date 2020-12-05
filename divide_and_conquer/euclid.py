# Реализуйте алгоритм Евклида с помощью рекурсии

def gcd(n, m):
  if n == m:
    return(n)
  else:
    if n > m:
      return gcd(n - m, m)
    else:
      return gcd(n, m - n)

n = int(input("Number:"))
m = int(input("Number:"))
print(gcd(n, m))