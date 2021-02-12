
def sum(N, result):
    if N == 0:
        mes = 'Sum of Your digits = ' + str(result)
        return mes
    else:
        result = result + N % 10
        N = N // 10
        return sum(N, result)
result = 0
N = int(input('Enter : '))
print(sum(N, result))
