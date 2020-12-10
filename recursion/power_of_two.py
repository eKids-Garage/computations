n = int(input('Введите число  : '))
def power_of_two(n):

	if n ==2:
		return "  YES"
	if n%2==0 :
		return power_of_two(n//2)
		
	elif n // 2 == 1:
		return "  no" 
	 

	if n % 2 != 0:
		return "  NO!"
print(power_of_two(n))


#print(power_of_two(1))#----------NO!
#print(power_of_two(3))#----------no
#print(power_of_two(12))#---------no
#print(power_of_two(10))#---------NO!
#print(power_of_two(16))#---------YES
#print(power_of_two(32))#---------YES
#print(power_of_two(256))#--------YES
#print(power_of_two(62))#---------NO!
#print(power_of_two(2121212))#----NO!
#print(power_of_two(44444444))#---NO!
#print(power_of_two(243))#--------NO!

