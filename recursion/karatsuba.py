def rec_mult(x, y, n):
    if n == 1:
        print("n = 1: x = {0}, y = {1}".format(x, y))
        return x*y
    else: 
        a = x // 10**(n//2)
        b = x % 10**(n//2)
        c = y // 10**(n//2)
        d = y % 10**(n//2)

        print("n = {4}: a = {0}, b = {1}, c = {2}, d = {3}".format(a, b, c, d, n))

        return 10**n * rec_mult(a, c, n//2) + 10**(n//2) * (rec_mult(a, d, n//2) + rec_mult(b, c, n//2)) + rec_mult(b, d, n//2)



def multiply(x, y):
  if x == 0:
    return 0
  if y == 0:
    return 0
  if x < 0:
     return -multiply(-x, y)
  if y < 0:
     return -multiply(x, -y)
  if x < 10 and y < 10:
     return x * y;
  
  x = str(x)
  y = str(y)
  XLen = len(x)
  YLen = len(y)
  maxLen = max(XLen, YLen)
  if maxLen % 2 != 0:
    maxLen = maxLen + 1
  halfLength = maxLen // 2
 
  xleft = int(x[:len(x) - halfLength])
  xright = int(x[len(x) - halfLength:])
  yleft = int(y[:len(y) - halfLength])
  yright = int(y[len(y) - halfLength:])
  n1 = multiply(yleft, xleft)
  n2 = multiply(yright, xright)
  n3 = (xleft + xright) * (yleft + yright)
  n4 = n3 - n2 - n1
  tens = 10**halfLength
  result = n1 * tens * tens + n4 * tens + n2
  return result

print(multiply(9656, 8578))
print(9656*8578)