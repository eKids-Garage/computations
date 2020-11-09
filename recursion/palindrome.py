# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.
c = 0
def is_palindrome(word, c):
  lenth = len(word)
  if  c == lenth//2:
    if c != 0:
      return "YES"
    else:
      return "NO"

    
    

  else:

    if word[lenth - c - 1] != word[c]:
      c = 0
      return "NO"
    else:
      word[lenth - c - 1] == word[c]
      c = c + 1
      return(is_palindrome(word, c))
    
    
    
    


  



 
word = str(input())
print(is_palindrome(word, c))