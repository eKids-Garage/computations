# Реши задачу Иосифа Флавия:
# где n - число солдат, k - шаг (2 - каждый второй (сосед), 3 - каждый третий и т.д.)
#
# 1. survive(n, k) - используя массив.
# 2. survive_num(n, k) - без использования массива


def survive(n, k):
  al = [True for i in range(n)]

  c = k-1
  a = n
  p = 0
  while a != 1:
    if c == 0 and al[p]:
      al[p] = False
      c = k-1
      a -= 1
    # Никто не юзает дебагеры, все юзать print и input
    #   print("Killed ", p)
    #   print(al, n)
    #   input()
    elif al[p]:
      c -= 1

    p += 1
    p = p % n

  return al.index(True) + 1


print(survive(10, 2))


def survive_num(n, k):
  # решу завтра
  pos = 0

  return pos
