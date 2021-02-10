def flav(w, k):
  index = 0

  while len(w) > 1:
    index = (index + k - 1) % len(w) 
    w.pop(index)
  return w[0]
