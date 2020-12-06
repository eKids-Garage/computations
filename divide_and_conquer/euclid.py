# Реализуйте алгоритм Евклида с помощью рекурсии

def euclidus(a, b): 
 while a!=b:
   if a>b:
     a=a-b
   else:
     b=b-a 
 return a       
   
          




         

print(euclidus(840,320))
