# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while


N = input("Type your number:")
N = int(N)
k = 1

#решить при помощи обычной рекурсии у меня, к сожалению, не получилось, поскольку я не смог бонально придумать решение без использования второго параметра

#tail recursion    
def is_prime_tail(N, k):
    
    k = k + 1
    
    if N == 2:
        return 'YES' #prime number
    
    if N == 3:
        return 'YES' #prime number
    
    if k < N:
        if N % k == 0:
            return 'NO' #composite number
    else:
        return 'YES' #prime number
    
    if k == N ** .5:
        return 'NO' #composite number
    
    if k == N // 2:
        return 'YES' #prime number
    else:
        return is_prime_tail(N, k)

print("Solving this task with help of tail recursion:") 
print(is_prime_tail(N, k))




k = 2 
#loop while
print("\nSolving this task with help of loop while:")
while k  != N // 2 or N != 3 or N != 2:
    
    
    if k < N:
        if N % k == 0:
            print('NO') #compositive number
            break
    else:
        print('YES') #prime number
        break
    
    if k == N ** .5:
        print('NO') #compositive number
        break
    k = k + 1