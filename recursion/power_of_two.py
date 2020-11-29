def func(N):
  if (N == 2):
    print ("YES")
    return
  if (N % 2 == 0):
    N = N // 2
    func(N)

  elif (N % 2 != 0):
    print ("NO")
    return
