#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!

def power_of_two(n):
    if n < 3:
        if n == 2:
            print ("YES")
        else:
            print("NO")
    else:
        n /= 2
        power_of_two(n)

n = int(input())
power_of_two(n)
