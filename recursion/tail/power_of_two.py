#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def is_power_of_two(N):
  return 'YES'


def is_power_of_two_tail(N, powered=1):
	if powered == N:
		return "YES"
	if powered > N:
		return "NO"
	powered = powered*2	 
	return is_power_of_two(N,powered)

N=int(input("Enter number \n"))	
print(is_power_of_two(N))

powered = 1
while True:
	if powered==N:
		print("YES")
		break
	if powered>N:
		print("NO")
		break
	powered=powered*2
	
