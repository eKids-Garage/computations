#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!

def is_power_of_two(n):
  n=n/2  
  if n==1:
    return 'YES'
  elif n>1:
    return is_power_of_two(n)
  elif n<1:
    return 'NO'

n=int(input("Введите число n:"))
print(is_power_of_two(n))