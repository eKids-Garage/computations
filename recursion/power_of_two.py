def power_of_two(N):
  c = 1
  while (c <= N):
    if c == N:
      return "YES"
    c = c * 2
  return "NO"


N = int(input())
print (power_of_two(N))