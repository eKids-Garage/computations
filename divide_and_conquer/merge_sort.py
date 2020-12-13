

def merge(a, b):
  c = []
  i = 0
  j = 0
  while len(c) != len(a) + len(b):
    if a[i] < b[j]:
      c.append(a[i])
      i += 1
    else:
      c.append(b[j])
      j += 1
    if j == len(b):
      while i < len(a):
        c.append(a[i])
        i += 1
    if i == len(a):
      while j < len(b):
        c.append(b[j])
        j += 1
  return c


def sort(a):
  if len(a) == 1:
    return a
  else:
    n = len(a) // 2
    return merge(sort(a[:n]), sort(a[n:]))
  return a


length = int(input())
a = []
for i in range(length):
  a.append(int(input()))
print (a)
print (sort(a))