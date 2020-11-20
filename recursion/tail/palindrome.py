# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def is_palindrome(word):
    return "YES"


def is_palindrome_tail(word, a):
  if a != len(word) // 2:
    if word[a] == word[len(word) - 1 - a]:
      is_palindrome_tail(word, a + 1)
    else:
      print("NO")
  else:
    print("YES")

word = input("Word:")
a = 0
is_palindrome_tail(word, a)

while a != len(word) // 2:
  if a + 1 == len(word) // 2:
    if word[a + 1] == word[len(word) - 1 - a]:
      print("YES")
      a = a + 1
  else:
    if word[a] == word[len(word) - 1 - a]:
      a = a + 1
    else:
      print("NO")
      a = len(word) // 2