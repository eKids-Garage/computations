def pal(word, c):
  l = len(word)
  if word[l - c - 1] == word[c]:
    if c == (l // 2):
      return ("YES")
    else:
      return pal(word, c + 1)
  else:
    return ("NO")


word = str(input())
c = 0
print(pal(word, c))
