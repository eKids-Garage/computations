# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

c=0
def is_palindrome(word):
  length=len(word)
  global c
  if word[length-c-1]==word[c]:
    c+=1
  else:
    return "NO"
  if c == length // 2:
    return "YES"
  return is_palindrome(word)

print(is_palindrome("ankna"))
