# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.
word = input("Введите слово:")
c=0
def is_palindrome(word):
  lenword = len(word)
  global c
  if word[lenword - c - 1] != word[c]:
    return "NO"
  else:
    if c==round(lenword/2):
      return "YES"
    else:
      c = c+1
      return (is_palindrome(word))
  
print (is_palindrome(word))
