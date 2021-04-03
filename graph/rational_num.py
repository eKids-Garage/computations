# Напишите функцию, которая складывает два рациональных числа
# Структуру данных для хранения чисел выберите и реализуйте сами



def NOD(a,b):
	if a < b:
		(a,b) = (b,a)
		
	if b == 0 :
		return a
	else :
		return NOD(a%b,b)


def sum_rat(a, b):
	num =b[1] * b[0] + a[1] * a[0]
	denum = b[1] * a[1]
	nod = NOD(num,denum)
	num//=nod
	denum//=nod
	return (num,
			denum)



print(
sum_rat((1,3),(1,6))
)









#вниз не смотреть
















class Rational:
	def __init__(self,numerator,denominator=1):
		self.numerator = numerator
		self.denominator = denominator
	
	def __add__(self,other):

		return Rational(
		other.denominator * other.numerator + self.denominator * self.numerator,
		other.denominator * self.denominator).simplify()



	def __mul__(self,other):
		return Rational(
			other.numerator * self.numerator,
			self.denominator * other.denominator
		).simplify()



	def __neg__(self):
		return Rational(self.numerator * -1,self.denominator).simplify()



	def __sub__(self,other):
		return (self + (-other)).simplify()


	def __truediv__(self,other):
		return Rational(
			self.numerator * other.denominator,
			self.denominator * other.numerator
		).simplify()


	def simplify(self):
		nod = NOD(self.numerator,self.denominator)
		self.numerator//=nod
		self.denominator//=nod
		return self

	def __repr__(self):
		self.simplify()
		return f"{self.numerator}/{self.denominator}"



