#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!

def is_power_of_two(N):
    if N == 1 or N == 2:
      return "yes"
    else:
      if N % 2 != 0:
        return "no"
      else:
        return is_power_of_two(N/2)
print(is_power_of_two(4))
print(is_power_of_two(3))
print(is_power_of_two(1))