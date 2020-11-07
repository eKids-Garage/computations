# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
N = input("Type your number:")
N = int(N)
c = 1

def is_prime(N):
    
    global c
    
    c = c + 1
    
    if N == 3:
        return 'YES' #prime number
    
    if c < N:
        if N % c == 0:
            return 'NO' #composite number
    
    if c == N ** .5:
        return 'NO' #composite number
    
    if c == N // 2:
        return 'YES' #prime number
    else:
        return is_prime(N)
    
    
print(is_prime(N))    