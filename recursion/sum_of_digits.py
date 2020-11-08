def sum(N):
  a = 0
  if N // 10 != 0:
    a = a + sum(N // 10) + N % 10
  else:
    a = a + N % 10
  return a
N = int(input())
print(sum(N))