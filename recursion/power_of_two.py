def is_power_of_two(N):
  if (N == 2, N == 1):
    print ("YES")
    return
  if (N % 2 == 0):
    N = N // 2
    is_power_of_two(N)

  elif (N % 2 != 0):
    print ("NO")
    return
