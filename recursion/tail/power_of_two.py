#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def is_power_of_two(n):
  if n / 2 == 1:
    print("YES")
  else:
    if n % 2 == 0:
      is_power_of_two(n / 2)
    else:
      print("NO")



def is_power_of_two_tail(n):
  if n / 2 == 1:
    print("YES")
  else:
    if n % 2 == 0:
      is_power_of_two_tail(n / 2)
    else:
      print("NO")

n = int(input("Number:"))
k = 2
is_power_of_two(n)
is_power_of_two_tail(n)

while n / 2 != 1:
  if (n / 2) / 2 == 1:
    print("YES")
    n = n / 2
  else:
    if n % 2 == 0:
      n = n / 2
    else:
      print("NO")
      n = 2