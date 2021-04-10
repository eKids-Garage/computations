# Напишите функцию, которая складывает два рациональных числа
# Структуру данных для хранения чисел выберите и реализуйте сами


def sum_rat(x, y):
  a, b = x
  c, d = y
  return (a * d + c * b, b * d)

rat_num1 = (2, 3)
rat_num2 = (4, 5)

print(sum_rat(rat_num1, rat_num2))

# ================================= А ЕСЛИ СДЕЛАТЬ ЭТО КРАСИВО


class RationalNum:
  def __init__(self, numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator

  def __str__(self):
    return str(self.numerator) + "/" + str(self.denominator)

  def __add__(self, other):
    return RationalNum(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)


x = RationalNum(2, 3)
y = RationalNum(4, 5)

print(x, "+", y, "=", x+y)