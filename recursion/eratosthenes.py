# Написать программу, которая находит все простые числа в заданном 
# интервале методом "Решето Эратосфена". 
# start и finish - границы диапазона (включительно).

#import math

def sieve(start, finish):
	if start<finish:
		#Create number table
		numbers = []
		i=start
		while i <= finish:
			numbers.append(i)
			i=i+1
		#######


		for curret in range(2, finish):
			power=2
			while curret*power<=finish :
				CurPow = curret*power
				if CurPow in numbers:
					print(curret, power, CurPow)
					numbers.remove(CurPow)
				power=power+1

		return numbers
	else:
		return "start > finish !!! Change values"

print(sieve(10, 20))

