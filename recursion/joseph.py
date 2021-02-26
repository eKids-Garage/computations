# Реши задачу Иосифа Флавия:
# где n - число солдат, k - шаг (2 - каждый второй (сосед), 3 - каждый третий и т.д.)
#
# 1. survive(n, k) - используя массив.
# 2. survive_num(n, k) - без использования массива


def survive(n, k):
    # создаём массив, значение элемента равно индексу, начало с 1
    arr = []
    for i in range(1, n + 1):
        arr.append(i)
    #print(arr)

    k = k - 1  # если каждый третий, то убиваем через 2
    next_kill = 0

    while (len(arr) > 1):
        next_kill += k

        # если массив закончился, то переходит на начало
        while (next_kill >= len(arr)):
            next_kill = next_kill - len(arr)

        # удаляем из массива, размер станет меньше на 1
        del arr[next_kill]
        #print(arr)

    return arr[0]


# Ссылка на объяснение рекурсивной реализации задачи Иосифа Флавия
# https://coderoad.ru/31775604/%D0%9E%D0%B1%D1%8A%D1%8F%D1%81%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%BA%D1%83%D1%80%D1%81%D0%B8%D0%B2%D0%BD%D0%BE%D0%B9-%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B8-%D0%98%D0%BE%D1%81%D0%B8%D1%84%D0%B0-%D0%A4%D0%BB%D0%B0%D0%B2%D0%B8%D1%8F
def survive_num(n, k):
    if (n == 1):
        return 1
    else:
        return (survive_num(n - 1, k) + k - 1) % n + 1


print(survive(410, 4))
print(survive_num(410, 4))
