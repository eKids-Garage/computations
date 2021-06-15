#задаем исходные переменные(количество цифр является степенью двойки)
a = int(input("Input a(count of numerals should be the power of 2): "))
b = int(input("Input b(count of numerals should be the power of 2): "))
n = 0

#находим количество цифр в числе
subNum = a
while subNum != 0:
  subNum = subNum//10
  n += 1

#функция в которой реализован алгоритм рекурсивного умножения
def rec_mult(x, y, n):
  if n == 1:
    return x*y
  else: 
    a = x // 10**(n//2)
    b = x % 10**(n//2)
    c = y // 10**(n//2)
    d = y % 10**(n//2)

    return 10**n * rec_mult(a, c, n//2) + 10**(n//2) * (rec_mult(a, d, n//2) + rec_mult(b, c, n//2)) + rec_mult(b, d, n//2)

#вывод конечного результата
print("a * b = {0}".format(rec_mult(a, b, n)))
