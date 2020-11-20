#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!

def is_power_of_two(N):
  if N == 2:
    return 'YES'
  elif N < 2:
    return 'NO'
  elif N > 2:
    return is_power_of_two(N/2)

print(is_power_of_two(512))