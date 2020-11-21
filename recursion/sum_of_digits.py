
def sum(N):
  if (N < 10):
    return N
  else:
    return N % 10 + sum (N // 10)

def sum_tail(N, s):
  if (N < 10):
    return s + N
  else:
    s += N % 10
    return sum_tail(N // 10, s)



N = int(input())
print (sum(N))

s = 0
print (sum_tail(N, s))

S = 0
while (N >= 10):
  S += N % 10
  N = N // 10
print (S + N)