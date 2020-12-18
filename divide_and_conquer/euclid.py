def euclid(a, b):
  if a == b:
    return(a)
  else:
    if a > b:
      return euclid(a - b, b)
    else:
      return euclid(a, b - a)
"""
print(euclid(12,6))         #6
print(euclid(1000,100))    #100
print(euclid(99,3))         #3
print(euclid(66,22))        #22
print(euclid(252, 441))     #63
print(euclid(441, 1080))    #9       
print(euclid(1080,720))     #360 
print(euclid(360,480))     # 120
print(euclid(7*8+8,8))        #8
"""
a= int(input("Введите 1 число:"))
b = int(input("Введите 2 число:"))
print(euclid(a,b))
