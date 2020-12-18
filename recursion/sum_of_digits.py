def sum(N, summ):
  if N > 10:
    digit = N % 10
    summ += digit
    N = N // 10
    sum(N, summ)
  else:
    print(summ+N)



sum(1234, 0)
