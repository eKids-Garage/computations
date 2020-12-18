
#list = array
import random
#   n  кол- во элементов 
n = random.randint(0,999) #  кол-во элементов генерируется 
list = []
for i in  range (0 , n) : # от 0 до кол-ва элементов в списке 
  list.append(random.randint(1,100))   # генерирует элементы массива и их туда добавляет
print('length = ' + str(n))
print(list)

def func(list):
  x = list[0]
  i = 0
  while i != len(list)-1:   # если I не в конце списка 
    #print('iteration :'+str(i+1))  
    if list[i] > list[i+1] : 
        x = list[i+1]   
        list[i+1] = list[i] 
        list[i] = x
        #print(list)
    else:
    	#print('ничего не делали')
    	i = i + 1
#pr=0 # кол-во проходов
i=0
while i < len(list)-1: # для всех элементов с первого по предпоследний
    if list[i] <= list[i+1]: # = для того если будут одинаковые числа 
      i = i + 1  
    else:
      func(list)
      #pr = pr + 1
      i = 0 # сбрасываем I
print('============================')
print(list)   
#print("\t"+"длина массива была :"+str(len(list)))
#print("\t"+"переставлений было:"+str(pr))
#print("\t"+"сэкономлено переставлений:"+str(len(list)-pr))
