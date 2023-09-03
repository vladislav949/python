# Циклы - Они позволяют выполнить одно и то же действие несколько раз подряд.

# Цикл for---------------------------------------------
for i in range(6): # i-переменная в диапазоне(range)-6
    print(i)
for i in range(1, 6): # i-переменная в диапазоне(range)-от 1 до 6
    print(i)
for i in range(1, 6, 2): # 3 параметр на сколько увеличивается переменная (1,3,5) (шаг в 2)
    print(i)

# Через цикл for можно перебирать определенные строки
count = 0
word = "Hello World!"
for i in word: # можно прописать и (for i in "Hello World") без переменной
    if i == "l":
        count += 1 # при нахождении символа (l) count увеличивается на 1
print("Count:", count) # в данном случае count=3, т.к. 3 символа были найдены

print("---------------------------------------------------------")
# Цикл while----------------------------------------------------
# Позволяет выполнять определенный код несколько раз подряд и кол-во выполнений можно определить самостоятельно.
# разница в for и while в формате записи
p = 5
while p <= 15:
    print(p)
    p += 2 # шаг в 2

# --------------------------------------------------------------
# Если пользователь напишет такое ключевое слово как (Stop), то устанавливается значение False
print("------------------------------------------------------------")
TruInfo = True
while TruInfo:
    if input("Enter data: ") == "Stop": # Цикл будет повторяться пока не получит (Stop)
        TruInfo = False

# Операторы в циклах -------------------------------------------
print("------------------------------------------------------------")
for i in range(1, 11):
    if i == 5:
        break   # позволяет выйти из цикла (выход из цикла как только дойдет до 5)

    if i % 2 ==0: # Если при делении на 2 остаток будет равен 0, останутся нечетные числа 1 и 3
        continue # пропускает одну определенную итерацию
    print(i)
print("-------------------------------------------------------------")

# Поиск символа в строке
found = None
for i in "hello":
    if i == "l":
        found = True # Если такой символ находится переменная=True
        break # Как только находится нужный символ - выход из цикла
else:
    found = False # Если такого символа нет, переменная=False
print(found)