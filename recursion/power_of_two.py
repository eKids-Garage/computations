#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!
N = int(input("введите натуральное число "))
def is_power_of_two(N):
  if N % 2 != 0:
    return "NO"
  if N == 2:
    return "YES"  
  return is_power_of_two(N//2)  
print(is_power_of_two(N))



  
