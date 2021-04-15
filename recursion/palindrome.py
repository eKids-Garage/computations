# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

def is_palindrome(word, c=0):
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
print(is_palindrome(slovo))

