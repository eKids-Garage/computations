# Реши задачу Иосифа Флавия:
# где n - число солдат, k - шаг (2 - каждый второй (сосед), 3 - каждый третий и т.д.)
# 
# 1. survive(n, k) - используя массив. 
# 2. survive_num(n, k) - без использования массива 



def survive(n, k, i=0 , mas=[]):


  if not i:
    mas = [o+1 for o in range(n)]
  if len(mas) < 2:
    return mas
  mas.remove(mas[(i + k - 1) % len(mas)])
  return survive(n, k, i+1 , mas)



    




def survive_num(n, k):
    pos = 0
    
    return pos


print(survive(3,2))