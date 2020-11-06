# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

def is_palindrome(word, c):
    if word[len(word) - 1 - c] != word[c]:
        return "NO"
    if c < len(word) / 2:
        return "YES"
    return is_palindrome(word, c + 1)

print(is_palindrome("abacaba", 0))