# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

def is_palindrome(word):
    return compare(word, 0)


def compare(word, c):
    if word[c] != word[len(word) - c - 1]:
        return "NO"
    if c == len(word) // 2:
        return "YES"
    return compare(word, c + 1)

    
print (is_palindrome("abcdedcba"))