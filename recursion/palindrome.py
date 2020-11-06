# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

def is_palindrome(word):
    if len(word)==1:
        return "YES"

    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])

    return  "NO"

