c = 0


def is_palindrome(word):
  Len = len(word)
  global c
  if c == Len // 2:
    print("YES")
    return 0
  if word[Len - c - 1] != word[c]:
      print('NO')
      return 0
  else: 
    c = c + 1
    is_palindrome(word)

is_palindrome('qwertyytrewq')