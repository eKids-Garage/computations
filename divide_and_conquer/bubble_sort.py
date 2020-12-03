# Реализуйте алгоритм сортировки пузырьком. Можете попробовать реализовать его
# как итеративно (используя цикл), так и рекурсивно.

#sorting, using while
def arraySortingWhile(array):
  i = 0
  n = 0
  while n < len(array):
    i = 0
    while i < len(array) - 1: 
      if array[i] > array[i + 1]:
        num = array[i + 1]
        array[i + 1] = array[i]
        array[i] = num
      i = i + 1
    n = n + 1
  return array

#К сожалению сортировку с помощью рекурсии в одну функцию у меня поместить не получилось
#sorting, using recurcion
def arraySortingRecursionFirstStep(array, n):
  i = 0
  if n < len(array):
    arraySortingRecursionSecondStep(array, i)
    n = n + 1
    arraySortingRecursionFirstStep(array, n)
  else:
    print(array)
def arraySortingRecursionSecondStep(array, i):
  if i < len(array) - 1:
    if array[i] > array[i + 1]:
          num = array[i + 1]
          array[i + 1] = array[i]
          array[i] = num
    i = i + 1
    arraySortingRecursionSecondStep(array, i)



array = [0, 5, 4, 8, 6, 1, 3, 2, 9, 7]
arrayTwo = [0, 5, 4, 8, 6, 1, 3, 2, 9, 7]
n = 0
print("Sorting, using while:")
print(arraySortingWhile(array))
print("Sorting, using recursion:")
arraySortingRecursionFirstStep(arrayTwo, n)


