#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!

def is_power_of_two(N):
  if N == 2 or N == 1:
    print("YES")
  else:
    if N % 2 == 0:
      N = N // 2
      is_power_of_two(N)
    else:
      print("NO")


is_power_of_two(3)
