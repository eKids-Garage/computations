#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!

n = int(input())
def is_power_of_two(n):
  while n!=1:
    if n==2 or n==1:
      print("YES")
    if n%2!=0:
      print ("NO")
      break
    else:
      n=n/2
      
is_power_of_two(n)
    
    
