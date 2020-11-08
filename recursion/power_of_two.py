def is_power_of_two(N):
  c = 0
  b = 2
  if N == 1 or N == 2:
    return "YES"
  elif N % 2 != 0:
    return "NO"
  else:
    while b <= N / 2:
      b = b * 2
      if (b == N / 2):
        return "YES"
        break
      elif (b > N / 2):
        return "NO"
        break
N = int(input())
print(is_power_of_two(N))