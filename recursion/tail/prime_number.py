# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def is_prime(n):
  return("YES")

    
def is_prime_tail(N, delitel=2):
	if delitel == N:
		return "YES"
	if N%delitel ==0 :
		return "NO"#,delitel
	else:
		delitel = delitel + 1
		return is_prime_tail(N,delitel)

number=int(input("Enter number \n"))
print(is_prime_tail(number))    

delitel=2
N=number
while True:
	if delitel == N:
		print("YES")
		break
	if N%delitel == 0:
		print("NO")
		break
	delitel = delitel + 1

