#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!

def is_power_of_two(N):
    return divide_by_2(N)

def divide_by_2(N):
    if (N == 1):
        return "YES"
    if (N % 2 != 0):
        return "NO"
    return divide_by_2(N/2)

print (is_power_of_two(32768))