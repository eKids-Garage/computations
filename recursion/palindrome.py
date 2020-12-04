# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

s=str(input())
l=len(s)
k=0
def is_palindrome(s, k):   
    if s[l-k-1] == s[k]:
        k = k + 1
    if s[l-k-1] != s[k]:
        return 'NO'
    if k == l//2:
        return 'YES'
    return is_palindrome(s, k)    
print(is_palindrome(s, k))
