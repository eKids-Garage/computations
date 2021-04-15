#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!

def is_power_of_two(N, powered=1):
	if powered == N:
		return "YES"
	if powered > N:
		return "NO"
	powered = powered*2	 
	return is_power_of_two(N,powered)

number=int(input("Enter number \n"))	
print(is_power_of_two(number))