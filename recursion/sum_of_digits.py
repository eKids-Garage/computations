N = int(input())
k = 1
def is_prime(a):
  i = 1
  c = 0
  if a > 3:
    while i <= a // 2:
      if a % i == 0 and i != 1:
        c = "NO"
        break;
      else:
        c = "YES"
      i = i + 1
  else:
    c = "YES" 
  return c
while k < N + 1:
  if(is_prime(k) == "YES" and N % k == 0):
    print(k)
  k = k + 1