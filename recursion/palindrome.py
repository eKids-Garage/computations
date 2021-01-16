# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

st = str(input())
c = 0
l = len(st)
def is_palindrome(word):
  global l
  global c
  if word[l-c-1]==word[c]:
    c+=1
  else:
    return "NO"
  if c == l // 2:
    return "YES"
  return is_palindrome(word)

print(is_palindrome(st))
    
