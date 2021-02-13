def flav(w, k):
  index = 0

  while len(w) > 1:
    index = (index + k - 1) % len(w) 
    w.pop(index)
  return w[0]


# n всегда равно 2
def survive(n, k):
  if n == 1:
    return 1
  fn = 2
  sn = 1
  while fn < n:
    fn += 1
    if sn + 2 > fn:
      sn = 1
    else:
      sn += 2
  return sn
