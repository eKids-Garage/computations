# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
a = 1
def is_prime(N):
	global a
	a += 1


	if a > N ** 0.5 :
		return "YES"
	elif N % a == 0:
		return "NO"
	else:
		return is_prime(N)

