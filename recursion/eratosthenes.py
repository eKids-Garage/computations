# Написать программу, которая находит все простые числа в заданном 
# интервале методом "Решето Эратосфена". 
# start и finish - границы диапазона (включительно).
def sieve(start, finish):
  arr = [num for num in range(2,finish)]
  for el in arr:
    if el > 0:
      for ind in range(el*2, len(arr), el):
          arr[ind] = 0
  def filt(num):
    return num!=0
  arr = list(filter(filt,arr))
  for i in range(len(arr)):
    if arr[i] >= start:
      return arr[i:]
