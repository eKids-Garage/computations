# Напишите функцию, которая складывает два рациональных числа
# Структуру данных для хранения чисел выберите и реализуйте сами

def nod(x,y):
  while x!=y:
    if x>y:
      x-=y
    else:
      y-=x
  return x

def print_rat(x):
  if x[1] != 1:
    return "{0}/{1}".format(x[0],x[1])
  else:
    return x[0]

def sum_rat(x,y):
  w=(x[0]*y[1]+y[0]*x[1])//nod((x[0]*y[1]+y[0]*x[1]),x[1]*y[1])
  q=x[1]*y[1]//nod((x[0]*y[1]+y[0]*x[1]),x[1]*y[1])
  c = (w,q)
  return print_rat(c)

print(sum_rat( (2,34),(1,17) ))
print(sum_rat( (1,5),(1,100) ))
print(sum_rat( (1,2),(1,2) ))
print(sum_rat( (1,5),(18,10) ))
print(sum_rat( (1,10),(198,20) ))

