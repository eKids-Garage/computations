# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

def is_palindrome(word, c):
  if(c != len(word) // 2):
    if(word[len(word) - c - 1] == word[c]):
      c = c + 1
      is_palindrome(word, c)
    else:
      print("No")
  else:
    print("Yes")


word = input("Input any word: ")
c = 0 
is_palindrome(word, c)
