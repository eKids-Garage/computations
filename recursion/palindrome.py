# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

word = input()
def symbolCheck(a, i=0) :
  if (i>=len(word)-i-1):
    print ('YES')
  
  elif (word[i]==word[len(word)-i-1]) :
    i=i+1
    symbolCheck(word, i)
  
  else : print ('NO')
symbolCheck(word)