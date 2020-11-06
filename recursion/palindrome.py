# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.
word = input(" введите словo ")
Len =len(word)
c = 0


def is_palindrome(word,Len,c):
  if word[Len - c - 1] != word[c]:
    return "NO"
  if c == Len//2:
    return "YES"


  return is_palindrome(word,Len,c+1)

  
print(is_palindrome(word,Len,c))