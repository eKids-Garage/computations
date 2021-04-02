x = 7676
y = 1034


def length(a):
  i = 1
  while a > 9:
    a = a // 10
    i += 1
  return i


def rec_mul (x,y):
  n = length(x)
  m = length(y)
  if n == 1 or m == 1:
    return x * y
  a = x // 10**(n//2)
  b = x % 10**(n//2)
  c = y // 10**(m//2)
  d = y % 10**(m//2)
  return (rec_mul(a,c) * 10**((n+m)//2)) + rec_mul(b,d) + (rec_mul(a,d) * 10**(n//2)) + (rec_mul(b,c) * 10**(m//2))



print(x * y)
print(rec_mul(x,y))