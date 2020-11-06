# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

N = str(input())
c = 0
def palindrome(a,c):
    if a[len(a) - c - 1] == a[c] and c <= len(a)//2 and len(a) > 1:
        return palindrome(a,c+1)
    elif (a[len(a) - c - 1] != a[c] and c <= len(a)//2) or len(a) <= 1:
        return "NO"
    else:
        return "YES"
print(palindrome(N,c))
