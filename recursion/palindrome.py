# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.
def is_palindrome(word):
  s=word[::-1]
  if word==s:
    print("Yes")
  else:
      print("No")

is_palindrome("ара")
