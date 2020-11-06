# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

def is_palindrome(word, c = 0):
    if not word[-(c + 1)] == word[c]:
        return "NO" 
    elif c >= len(word) // 2:
        return "YES"
    else:
        return is_palindrome(word, c + 1)

