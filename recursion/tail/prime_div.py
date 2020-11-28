# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

#извините, но решить задачу обычной рекурсией у меня не получилось
def dividors(N):
    return 0

def dividors_tail(N, k):
    if(N != 1):
      if (N % k == 0):
        N = N / k
        print(k)
        k = 2
        dividors_tail(N, k)
      else:
        k = k + 1
        dividors_tail(N, k)

def dividors_while(N, k):
    while N > 1:
      if (N % k == 0):
        N = N / k
        print(k)
        k = 2
      else:
        k = k + 1

N = int(input("Input any number: "))
k = 2
print("Tail recursion: ")
dividors_tail(N, k)
print("While: ")
dividors_while(N, k)
