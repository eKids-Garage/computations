num1 = input("Введите число 1: ")
num2 = input("Введите число 2: ")

min_operation=1
def karatsuba(a, b):
  length = max(len(a), len(b))
  i = 1
  while length/2 > 1:
    length /= 2
    i+=1
  f_length = 2**i
  num1="0"*(f_length-len(a)) + a
  num2="0"*(f_length-len(b)) + b
  return counter(num1,num2, len(num1))

def broke_multiplication(n1, n2):  
  splitter1 = int(len(n1)/2)
  splitter2 = int(len(n2)/2)
  n1_A = n1[:splitter1]
  n1_B = n1[splitter1:]
  n2_X = n2[:splitter2]
  n2_Y = n2[splitter2:]
  return ((n1_A, n1_B), (n2_X, n2_Y))


def counter(X,Y, n):
  
  if len(X) <= min_operation: 
    return int(X)*int(Y)

  ((X1, X2),(Y1, Y2)) = broke_multiplication(X,Y)
  if len(X)/2 >=min_operation:
    composition1 = counter(X1,Y1, n//2)
    composition2 = counter(X1, Y2, n//2)
    composition3 = counter(X2, Y1, n//2)
    composition4 = counter(X2, Y2, n//2)
    
  result = 10**n *composition1 + 10**(n//2)*(composition2+composition3) + composition4


  return int(result)
print(karatsuba(num1, num2))