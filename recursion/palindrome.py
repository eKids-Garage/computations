# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.


word = input()

c=0


def is_palindrome(word, c):
    if c != round(len(word) / 2):
        if word[c] == word[len(word) - 1 - c]:
           c += 1
           is_palindrome(word, c=c)
        else:
            print("NO")
    else:
        print("YES")

is_palindrome(word, c=c)        