#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!

def is_power_of_two(N):
  if N == 1:
    return 'YES'
  elif N < 1:
    return 'NO'
  else:
    return is_power_of_two(N / 2)

print(is_power_of_two(1)) # yes
print(is_power_of_two(2)) # yes
print(is_power_of_two(4)) # yes
print(is_power_of_two(16)) # yes
print(is_power_of_two(1024)) # yes
print(is_power_of_two(0)) # no
print(is_power_of_two(3)) # no
print(is_power_of_two(10)) # no
print(is_power_of_two(1028)) # no