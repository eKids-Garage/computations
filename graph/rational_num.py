a = []
a.append(int(input("Input a - numerator:")))
a.append(int(input("Input a - denominator:")))

b = []
b.append(int(input("Input b - numerator:")))
b.append(int(input("Input b - denominator:")))

def sum_rat(a, b):
  return [a[0]*b[1] + b[0]*a[1], a[1]*b[1]]

def sum_print(sum):
  print("{0}/{1}".format(sum[0], sum[1]))

sum = sum_rat(a, b)
sum_print(sum)
  
