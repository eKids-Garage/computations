# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 

def is_prime(N, c):
    if N % c == 0:
        return "NO"
    if c > N**0.5:
        return "YES"
    return is_prime(N, c + 1)

print(is_prime(9973, 2))