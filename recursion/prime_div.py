# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  

def prime_div(N, k):
	if k>N:
		pass
	elif not N > 1:
		prime_div(N, k + 1)
	elif N % k == 0:
		print(k)
		prime_div(N/k, k)
	else:
		prime_div(N, k + 1)

prime_div(230230, 2)
