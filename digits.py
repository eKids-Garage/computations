def reverse(N):
    if N < 10:
        return N
    else:
        print(N % 10)
        return (reverse(N // 10))


def direct(N):
    if N < 10:
      return N
    else:
      print (direct(N // 10))
      return N % 10

print(reverse(304))
print(direct(304))