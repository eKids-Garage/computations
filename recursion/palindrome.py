# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

def is_palindrome(word, a):
  if a != len(word) // 2:
    if word[a] == word[len(word) - 1 - a]:
      a = a + 1
      is_palindrome(word, a)
    else:
      print("NO")
  else:
    print("YES")

    
word = input("Word:")
a = 0
is_palindrome(word, a)