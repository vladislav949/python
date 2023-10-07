# Задание № 1: -----------------------------
def sq(x):
    return x ** 2


print(sq(2))


# Задание № 2: -----------------------------
def print_string(string):
    print(string)


print_string("1, 2, 3")


# Задание № 3: -----------------------------
def f(x, y, z, p=2, o=1):
    return x + y + z + p + o


result = f(1, 2, 3)
print(result)


# Задание № 4: ------------------------------
def funct1(x):
    return x / 2


def funct2(x):
    return x * 4


y = funct1(8)
z = funct2(y)

print(z)


# Задание 5: --------------------------------
def convert(j):
    """ Преобразует строку в целое число.
        :параметр string: строка.
        :return: Cтрока, преобразованная в целое число.
        """
    try:
        return float(j)
    except ValueError:
        print("Не удалось преобразовать строку в число с плавающей точкой.")


j = convert("55.5")
print(j)
