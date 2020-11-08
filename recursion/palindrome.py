def is_palindrome(word):
  a = len(word)
  c = 1
  b = (a // 2) + 1
  d = ""
  if a % 2 == 0:
    d = "NO"
  else:
    while c <= b:
      if word[c] != word[a - c - 1]:
        d = "NO"
        break
      else:
        d = "YES"
      c = c + 1
  return d

word = str(input())
print(is_palindrome(word))