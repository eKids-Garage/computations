# Напишите функцию, которая складывает два рациональных числа
# Структуру данных для хранения чисел выберите и реализуйте сами

def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a        
    return(a)

def rat_num(x, y=1):
  if y==1:
    return [x,1]
  else:
    n=gcd(x,y)
    num=[int(x/n), int(y/n)]
    return (num)

def rat_sum(a=[0,1],b=[0,1]):
  print(rat_num(a[0]*b[1]+a[1]*b[0], a[1]*b[1]))

rat_sum(rat_num(11,124), rat_num(22,222))
