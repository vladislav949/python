# print("вывод текста")
# sep=""(разделитель), sep="символ разделения"
# end="" конец строки (перевод на новую строку "\n")
print("first line: ", 1, 7, ".", sep="|", end="\n")
print("second line \"2\": ")  # \ перед кавычкой = обычный символ

# Test 1 --------------------------------------------------------------
print('test line 1 "t"')  # либо поставить '' кавычки ('test line "t"')
print('test line 2 \'t\'')
print('test \nl\ni\nn\ne \n3 \n\'t\'')  # перевод на новую строку
print("test line \\3\\")  # \\

# Математические действия ---------------------------------------------
print("5+5=", 5 + 5)
print("5 в степени 2 =", 5 ** 2)  # Возведение в степень ** (2 квадрат,3 куб)
print("Округление к целому 5:3 =", 5 // 3)  # (//) Округление к целому при делении

# Математические функции ----------------------------------------------
print("Минимальное значение", min(5, 2, -1, 15))  # Выводит минимальный элемент
print("Максимальное значение", max(5, 2, -1, 15))  # Выводит максимальный элемент
print("По модулю", abs(-5))  # Находит число по модулям
print("Возведение 5 в степень 3 =", pow(5, 3))  # Возведение в степень
print("Округление до близжайшего целого 5:3 =", round(5 / 3))  # Окрулгение числа до близжайщего целого

# Получение данных пользователя ----------------------------------------
# input("Введите ваше число") # Получение от пользователя каких-либо значений


# Переменные и типы данных ---------------------------------------------
number = 5  # - (number - 1 переменная). Нельзя использовать $%# символы
print("переменная", number)

digit = 7.55  # digit - 2 переменная
word = "Результат:"  # word - 3 переменная
print(word, digit)  # Вывод двух переменных

boolean = True  # Булевый тип данных. От True/False Зависит какая часть кода будет выполняться дальше
print(word, boolean)

del number  # удаление переменной

number = 7
print("переменная", number)

# Типы данных
number = 5  # Создавая некое целое число, значит тип данных (int)
digit = 7.55  # Создавая число с точкой (float)
word = "Результат:"  # Создавая строку (string)
boolean = True  # Создавая булевую переменную (bool)
# Сложение разных переменных невозможно, пример print(word + boolean) Разные типы данных
print(word + str(boolean))  # происходит преобразование в строку string
str_num = "5"  # тип str (string)
print(number + int(str_num))  # Преобразование в int (к число 5-number добавлено число 5-str_num)
print(word + str(number + int(str_num)))
