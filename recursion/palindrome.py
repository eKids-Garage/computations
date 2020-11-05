# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

word = input()
def is_palindrome(word,i=0) :
  if (i>=len(word)-i-1):
    print ('YES')
  
  elif (word[i]==word[len(word)-i-1]) :
    i=i+1
    is_palindrome(word, i)
  
  else : print ('NO')
is_palindrome(word)