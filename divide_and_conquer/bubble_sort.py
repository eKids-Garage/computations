# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.

from random import randint
N = int(input('введите длинну массива ')) #длинна массива;) незнаю зачем но я её сделял
O = int(input('введите максимальное число которое может быть в массиве ')) #незнаю зачем но я это сделял
a = []

def bubble(array):
  for i in range(N-1):
    for j in range(N-i-1):
      if array[j] > array[j+1]:
        K = array[j]
        array[j] = array[j+1]
        array[j+1] = K

for i in range(N):
  a.append(randint(1, O))

print(a)
bubble(a)
print(a)

