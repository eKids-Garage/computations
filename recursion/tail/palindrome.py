# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def is_palindrome(word,c=0):
  length=len(word)
  if c == length // 2:
    return "YES"
  if word[length-c-1]==word[c] and is_palindrome_tail(word,c+1) == "YES":
    return "YES"
  else:
    return "NO"


def is_palindrome_tail(word, c = 0):
  length=len(word)
  if c == length // 2:
    return "YES"
  if word[length-c-1]==word[c]:
    return is_palindrome_tail(word,c+1)
  else:
    return "NO"

#while
word="ABA"
c=0
res="-"
while c < len(word) // 2+1:
  length=len(word)
  if c == length // 2:
    res = "YES"
    break
  if word[length-c-1]==word[c]:
    c+=1
  else:
    res = "NO" 
    break
print(res,"\n") 
#while

print(is_palindrome("ABCBA"))
print(is_palindrome_tail("ABCBA"))