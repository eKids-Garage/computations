def palindrom(word,i,a):
    if len(word)-i  < 2:
        return "Yes"
    elif word[a] == word[i]:
            if i < len(word)//2 - 1:
                i = i + 1
                a = a - 1
                palindrom(word,i,a)
            return "YES"
    else:
            return "NO"

word= [] # массив
word = input("введите слово : ")
i = 0 # порядок элемента 
a = -1 # порядок элементов с конца
print(palindrom(word,i,a))

