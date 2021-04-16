# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def is_palindrome(word):
	  return "YES"


def is_palindrome_tail(word, c=0):
	Len = len(word)

	if word[Len-c-1] == word[c]:
		if c == Len//2:
			return "YES"
		else:	
			c = c + 1
			return is_palindrome(word,c)
	else:
		return "NO"	



slovo = input("Enter Word \n")
print(is_palindrome_tail(slovo))
Len = len(slovo)
c=0

while True:
	if slovo[Len-c-1] != slovo[c]:
		print("NO")
		break
	if c==Len//2:
		print("YES")	
		break
	else:
		c=c+1


