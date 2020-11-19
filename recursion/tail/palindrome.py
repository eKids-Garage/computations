# Дано слово, состоящее только из строчных латинских букв.
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

def is_palindrome(word):
    if len(word) == 0:
        return True

    isPalid = is_palindrome(word[1:-1])
    return isPalid and word[0] == word[-1]


def is_palindrome_tail(word, n = 0):
    if n > len(word) // 2:
        return "YES"

    if word[n] == word[-(n + 1)]:
        return is_palindrome_tail(word, n+1)
    return "NO"

# WHILE
def is_palindrome_while(word):
    n = 0
    while True:
        if n > len(word) // 2:
            return "YES" 
        if word[n] != word[-(n + 1)]:
            return "NO"
        n += 1


palinodroms = [
    "wow",
    "wowow",
    "omggmo",
    "hahah"
]

notPalinadroms = [
    "wfsfsf",
    "magic",
    "word",
    "wowo"
]

for palinodrom in palinodroms:
    assert is_palindrome_tail(palinodrom) == "YES"
    assert is_palindrome_while(palinodrom) == "YES"
    assert is_palindrome(palinodrom)

for palinodrom in notPalinadroms:
    assert not is_palindrome_tail(palinodrom) == "YES"
    assert not is_palindrome_while(palinodrom) == "YES"
    assert not is_palindrome(palinodrom)

print("All is ok")