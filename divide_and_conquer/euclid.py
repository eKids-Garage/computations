from random import randint
# Реализуйте алгоритм Евклида с помощью рекурсии

def euclidus(a, b):
    return GCD(a,b)

def GCD(*elements):
	if len(elements)==1:
		return elements[0]
	if len(elements) == 0: return 1
	elif len(elements) >2:
		middle = int(len(elements)/2)
		return GCD(
			GCD(*elements[middle:]),
			GCD(*elements[:middle])
		)
	(a,b) = elements
	
	if a < b:
		(a,b) = (b,a)
	if b == 0 :
		return a
	else :
		return GCD(a%b,b)





def main():
	#elements = [randint(0,1000) for i in range(randint(0,10))]
	#gcd = GCD(*elements)

	a,b = randint(0,1000),randint(0,1000)
	print(f"a: {a}, b: {b}")
	gcd = GCD(a,b)
	print(f"GCD: {gcd}")

	return 0

if __name__ == '__main__':
	main()