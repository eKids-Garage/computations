# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 


def is_prime(N,k):
    print(k)
    if k == N:
        return 'Yes'
    else:
        if N != k :
            if N % k == 0:
                return 'No'
            else:
                k = k + 1 
                return is_prime(N,k)
N = int(input('Enter your number : '))
k = 2  

print(is_prime(N,k))
