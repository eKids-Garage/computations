def length(a):
  i = 1
  while a > 9:
    a = a // 10
    i += 1
  return i


def rec_mul(n, m):
  x = length(n)
  y = length(m)
  if (x < 2 or y < 2):
    return n * m
  a = n // 10**(x//2)
  b = n % 10**(x//2)
  c = m // 10**(y//2)
  d = m % 10**(y//2)
  return (rec_mul(a,c) * 10**((x+y)//2)) + (rec_mul(a,d) * 10**(x//2)) + (rec_mul(b,c) * 10**(y//2)) + rec_mul(b,d)


a = int(input())
b = int(input())
print (rec_mul(a, b))