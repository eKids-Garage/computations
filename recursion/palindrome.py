# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

st = str(input())
def is_palindrome(word):
  l = len(st)
  c = 0
  k=0
  while c!= l:
    if st[c] == st[l-c-1]:
      c+=1
      k+=1
    else:
      print ("NO")
      break
  if k == l:
    print("YES")

is_palindrome(st)
    
