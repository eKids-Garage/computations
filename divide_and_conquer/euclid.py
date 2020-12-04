# Реализуйте алгоритм Евклида с помощью рекурсии


#data retrieval
side_1 = input("Type the 1st side of your rectangle:")
side_1 = int(side_1)

side_2 = input("Type the second side of your rectangle:")
side_2 = int(side_2)


#main function
def euclidus(a, b):
    if a == b:
        return a
    if a > b:
        return euclidus(a-b, b)
    if a < b:
        return euclidus(a, b-a)


#response output
print( 'You will get square ' + str(euclidus(side_1, side_2)) + '×' +
       str(euclidus(side_1, side_2)))    