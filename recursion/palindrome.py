# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

def is_palindrome(word, c = 0):
  if c == len(word) // 2:
    print("YES") 
  elif word[len(word) - c - 1] != word[c]:
    print("NO")
  else:
    is_palindrome(word, c + 1)

is_palindrome("a")
is_palindrome("")
is_palindrome("aa")
is_palindrome("abcba")
is_palindrome("abccba")

is_palindrome("ab")
is_palindrome("abcbc")