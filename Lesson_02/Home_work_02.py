# Задача 1

# Напишіть программу "Касир в кінотеватрі", яка попросить користувача ввести свій вік
# (можна використати константу або функцію input(),
# на екран має бути виведено лише одне повідомлення).
# якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
# якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# якщо від 16 до 65 то зробіть якесь вітальне повідомлення, на ваш розсуд.
# якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"

# age = int(input("Введіть свій вік: "))
# if age <= 7:
#     print("Де твої батьки?")
# elif age >=7 and age <= 16:
#     print("Це фільм для дорослих!")
# elif age >16 and age <=64:
#     print("Ласкаво просимо!!!")
# elif age >=65:
#     print("Покажіть пенсійне посвідчення!")
# ==========================================================================================

# Задача 2

# Текстова в чому різниця між is та ==?
# is - перевіряє чи відносяться змінні до одного ID/комірки в пам'яті,
# а == - порівнюе фактичні значення в цих змінних

# ==========================================================================================


# Задача 3
# Напишіть програму яка в користувача запитує два числа(можуть бути числа типу інт, а можуть бути в стр).
# Потім запитує це стр чи інт і в залежності від відповіді конкатенує їх або додає і повертає результат
# перемножений на три.
# якщо після конкатенації отримали 10 то перемноживши на 3 отримаємо 30.
#

print("Введіть два числа")
var1 = input("Перше число: ")
var2 = input("Друге число: ")
type_var = input("Напишіть який тип данних ви ввели (str чи int)? : ")
if type_var.lower() == "int":
    i = (int(var1) + int(var2))
    print(i * 3)
else:
    i = var1 + var2
    print(int(i) * 3)

# ==========================================================================================


# Не оцінюється
#
# 1) Напишіть на 50-100 слів відповідь на питання як пройшов ваш день, що ви робили сьогодні на англійській мові.
# Запишіть його собі на диктофон в озвучці наприклад гугл перекладача і
# повторюйте що б ви змогли відповісти на це питання.
# Якщо буде робити через чатджпт вкажіть що рівень слів повинен бути B2. - Це можете нікому не відправляти.
#
# 2) Скиньте ваш профіль лінкедін в групу телеграму і додайте інші профілі учасників які є в телеграмі.
# https://www.linkedin.com/in/metel-sky/   - Скинув

# Додаткове завдання хто хоче поглибити знання (воно не оцінюється).
#
# 1) Так як я у відео міняв значення за допомогою віднімання та додавання,
# зробіть це ж саме за допомогою множення.
# Там дуже простий алгоритм вирішення. Спробуйте в ньому розібратись

#

# 2) Напишіть програму яка буде приймати квадратне рівняння і розвязувати його.
# Памятайте що там є декілька випадків по іксам. Завдання не складне але обьємне.
# Подумайте як прийняти дані від користувача, ну і над рештою).
