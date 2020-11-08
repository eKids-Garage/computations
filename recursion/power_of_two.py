def power_of_two(N):
  c = 1
  while (c < N):
    c = c * 2
    if c == N:
      return "YES"
  return "NO"


N = int(input())
print (power_of_two(N))