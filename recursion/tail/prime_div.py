# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def dividors(n,k=2):
	if n/k<k:
		return [n]
	if n%k == 0:
		return [k] + dividors(n//k)
	if n%k !=0:	
		k=k+1
		return dividors(n,k)

    


def divide_tail(N, k=2):
	if N==1:
		return 0
	if N%k == 0:
		print(k)
		N=N//k
		return divide_tail(N)
	if N%k != 0:
		k=k+1
		return divide_tail(N,k)

print(dividors(24))
divide_tail(24)
N=24

k=2
while N>1:
	if N%k==0:
		print(k)
		N=N//k
		k=2
	else:
		k=k+1	
