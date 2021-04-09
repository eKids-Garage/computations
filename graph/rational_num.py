def red (a, b):
	if a > b :
		return red(a - b, b)
	elif a < b :
		return red(a, b - a)
	else:
		return a

def rat_num(a, b):
	x = a[0] * b[1] + b[0] * a[1]
	y = a[1] * b[1]
	c = red(x, y)
	return (x // c, y // c)


x = (int(input()), int(input()))
y = (int(input()), int(input()))
print (x[0], '/', x[1])
print ('+')
print (y[0], '/', y[1])
print ('=')
k = rat_num(x, y)
if (k[0] % k[1] == 0):
	print (k[0] // k[1])
elif (k[0] > k[1]):
	print (k[0] // k[1], '+', k[0] - k[0] // k[1] * k[1], '/', k[1])
else:
	print (k[0], '/', k[1])