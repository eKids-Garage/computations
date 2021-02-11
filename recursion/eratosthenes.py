# Написать программу, которая находит все простые числа в заданном 
# интервале методом "Решето Эратосфена". 
# start и finish - границы диапазона (включительно).

print('enter the first number')
num1 = int(input())
print('enter the last number')
num = int(input())


def sieve(start, finish):
  numbers = []
  while start<=finish:
    numbers.append(start)
    start = start+1
  #print(numbers)

  i = 0
  numtest = 2
  if 1 in numbers:
    numbers.remove(1)
  else:
    breakpoint
  while numtest < numbers[len(numbers) - 2]:
    while len(numbers) > i:
      if numbers[i] != numtest and numbers[i]%numtest == 0:
        numbers.pop(i)
      else:
        i = i + 1

    i = 0
    for nextnum in range(len(numbers)):
      if numbers[nextnum] > numtest:
        numtest = numbers[nextnum]
      else:
        breakpoint
  return numbers

print("here is the prime number in between", num1, "and", num, sieve(num1, num))

