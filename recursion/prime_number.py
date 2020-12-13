# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 

def is_prime(x, d=2):
    if x == 1:
        print("NO")
        return 
    if d < x:
        if x % d == 0:
            print("NO")
        else: 
            d += 1
            is_prime(x, d)
    elif d == x:       
        print("YES")