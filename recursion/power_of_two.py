#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!
N = int(input("Введите число:"))
def is_power_of_two(n):
  if n == 1:
    return 'YES'
  if n % 2 != 0:
    return 'NO'
  return is_power_of_two(n//2)

print(is_power_of_two(N))