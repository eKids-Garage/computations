# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

word = input("Type your word:")
Len = len(word)
c = 0

def is_palindrome(word, c):
       
    if word[Len - c - 1] == word[c]:
        c = c + 1
    
    if word [Len - c - 1] != word[c]:
        return 'NO'
    
    if c == Len // 2:
        return 'YES'
    
    return is_palindrome(word, c)    
    
print(is_palindrome(word, c))    
