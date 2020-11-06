#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!

def is_power_of_two(N):
    if (N==1):
      print ('YES')
    elif(N%2==1):
      print('NO')
    else: 
      N=N/2
      is_power_of_two(N)
num=input()
num=int(num)
is_power_of_two(num)