# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.
Word = input("Введите слово:")
def is_palindrome(someWord, c = 0):
  if someWord[len(someWord) - c - 1] != someWord[c]:
    return "NO"
  elif c == len(someWord) // 2: 
    return "YES"
  else:
    return is_palindrome(someWord, c + 1)


print(is_palindrome(Word))

