#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!

def is_power_of_two(N):
    if N == 1:
        return "YES"
    if N % 2 != 0:
        return "NO"
    return is_power_of_two(N / 2)

print(is_power_of_two(1024))
