def rec_mult(x, y, n):
	if n == 1:
		return x * y

	a = x // 10 ** (n//2)
	b = x % 10 ** (n//2)
	c = y // 10 ** (n//2)
	d = y % 10 ** (n//2)

	return 10**n * rec_mult(a, c, n//2) + 10**(n//2) * (rec_mult(a, d, n//2) + rec_mult(b, c, n//2)) + rec_mult(b, d, n//2)
