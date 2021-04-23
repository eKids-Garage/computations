# Реализуйте алгоритм Евклида с помощью рекурсии

def euclidus(a, b):
	if a==b:
		return a
	if a>b:
		return euclidus(a-b,b)
	if a<b:
		return euclidus(a,b-a)		

print(euclidus(10,15))		