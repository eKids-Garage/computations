# Реализуйте алгоритм рекурсивного умножения.
# Попробуйте реализовать его для чисел любого размера,
# но также можно ограничиться числами с размерностью
# степень двойки: 2, 4, 8, 16 и т.д.


def ss(a, b):
  return str(int(a) + int(b))


def rec_mul(x, y):
  if len(x) == 2 and len(y) == 2:
    return str(int(x) * int(y))

  targetlen = max(len(x), len(y))
  if targetlen % 2 == 1:
    targetlen += 1

  x = "0" * (targetlen - len(x)) + x
  y = "0" * (targetlen - len(y)) + y

  a = x[:len(x) // 2]
  b = x[len(x) // 2:]

  c = y[:len(y) // 2]
  d = y[len(y) // 2:]

  # print(a, b, c, d)
  # print(rec_mul(a, c) + "0" * targetlen)
  # print(rec_mul(a, d) + "0" * (targetlen // 2))
  # print(rec_mul(b, c) + "0" * (targetlen // 2))
  # print(rec_mul(b, d))
  # print()

  return ss(
    ss(
      rec_mul(a, c) + "0" * targetlen,
      ss(
        rec_mul(a, d),
        rec_mul(c, b)
      ) + "0" * (targetlen // 2)
    ), 
    rec_mul(b, d)
  )


print(rec_mul("123", "456"))