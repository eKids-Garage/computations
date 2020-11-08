def is_prime(N):
  i = 1
  c = 0
  if N > 3:
    while i <= N // 2:
      if N % i == 0 and i != 1:
        c = "NO"
        break;
      else:
        c = "YES"
      i = i + 1
  else:
    c = "YES" 
  return c
N = int(input())
print(is_prime(N))