# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

N = input("Type your number:")
N = int(N)
k = 2

#Не смог решить задачу при помощи обычной рекурсии, так как не понимаю, как можно решить эту задачу без передачи второго аргумента


def dividors_tail(N, k):
    if N * k != k:
        if N % k == 0:
            print(k)
            N = N // k
            dividors_tail(N, k)
        else:
            k = k + 1
            dividors_tail(N, k)

print("Solving problem with help of tail recursion:")
dividors_tail(N, k)


print("\nSolving problem with help of while loop:")      

while N * k != k:
  if N % k == 0:
      print(str(k))
      N = N // k
  else:
      k = k + 1

     