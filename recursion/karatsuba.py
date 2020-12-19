def num_count(x):
  num = 0
  while(x > 10):
    x //= 10
    num += 1
  num += 1
  return num


def karatsuba(x, y):
  a = x // 10 ** (num_count(x) // 2)
  b = x % 10 ** (num_count(x) // 2)
  c = y // 10 ** (num_count(y) // 2)
  d = y % 10 ** (num_count(y) // 2)

  if (x == 10):
      a = 1
  if (y == 10):
      c = 1

  print(a, b, c, d)
  
  num = num_count(x)
  res1 = a * c
  res2 = b * d
  res3 = (a + b) * (c + d)
  res4 = res3 - res2 - res1
  return(res1 * (10 ** num)) + (res4 * (10 ** (num // 2)) + res2)
  
