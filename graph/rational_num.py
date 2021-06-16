def euclid(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def printRatsio(number):
        print('{0}/{1}'.format(number[0], number[1]))

def readRatsio(a):
    c = ''
    result = []
    for i in a:
        try:
            if type(int(i)) == int:
                c = c + i
        except Exception:
            result.append(int(c))
            c = ""
    if len(c) > 0:
        result.append(int(c))
    return result

def ratsio(a, b):
    result = [a[0] * b[1] + b[0] * a[1], b[1] * a[1]]
    socrat = euclid(result[0], result[1])
    if result[0] == result[1]:
        result = 1
    else:
        result[0] = result[0] / socrat
        result[1] = result[1] / socrat
    return result

a = input('Первая дробь: ') # 1/2
b = input('Вторая дробь: ')
a = readRatsio(a)
b = readRatsio(b)
printRatsio(ratsio(a, b))