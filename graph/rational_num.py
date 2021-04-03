def GCD(a, b):
	if a == b:
		return a
	elif a > b:
		a -= b
		return GCD(a, b)
	else:
		b -= a
		return GCD(a, b)

def LCM(a, b):
	return a * b // GCD(a, b)



def sum_ratio(a, b):
	if a[1] == b[1]:
		res0 = a[0] + b[0]
		res = [res0, a[1]]
		gcd = GCD(res[0], res[1])

		if gcd != 0:
			res[0] //= gcd
			res[1] //= gcd
		
		if res[0] > res[1]:
			int_part = res[0] // res[1]
			res[0] = res[0] % res[1] 
			
			if res[0] == 0:
				return int_part

			return "{} {}/{}".format(int_part, res[0], res[1])

		return "{}/{}".format(res[0], res[1])

	else:
		lcm = LCM(a[1], b[1])
		x = lcm // a[1]
		y = lcm // b [1]
		a[0] *= x 
		a[1] *= x
		b[0] *= y
		b[1] *= y	
		return sum_ratio(a, b)	
