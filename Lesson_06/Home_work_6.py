# Домашка
#
# Візьміть дві задачі з попередніх уроків,
# перша легка по вирішенню(декілька стрічок),
# друга більш складна і перепишіть їх на функції.
# Памятайте про Атамарність та god object.
# Там де написано що користувач має щось ввести то перероблюємо на функція приймає.
# Подивіться може можна за допомогою функції спростити код.
# В домашку вставте будь ласка опис задачі (далі(один з наступних уроків)
# буде домашка вашу домашку покрити тестами, але ми трохи поміняємо варіанти).

# ============================================================================================

# Home work 4
# Задача 3
# Напишіть програму Банкомат. Втсановіть пін код для користувача(зробимо це константою).
# Запитайте в користувача Пін якщо він введе три рази не вірно
# то напишіть що карта заблокована.
# Використовуйте цикл while.


# PIN = 1515
#
#
# def pin_on(pin: int):
#     n = 0
#     while n < 3:
#         if n == 2 and pin != 1515:
#             print("Карта заблокована!!!")
#             return
#         elif pin != PIN:
#             n += 1
#             print(f"Не правильний пін спробуйте ще, у вас залишилось {3 - n} спроб.")
#             pin = int(input("Введіть ПІН: "))
#         else:
#             print("Ласкаво просимо до вашого особистого кабінету")
#             return
#
#
# pin_on(input("Введіть ПІН: "))

# ============================================================================================

# Home work 5
# Зробіть словник де буде табличка множення,
# додавання, ділення, і віднімання, чисел від 2 до 9(включно).
# Так як робили на уроці.
# Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
#
# Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити
# (додавання, віднімання, множення, ділення). і виведіть йому цю табличку.


dict_1 = {'+': {}, '-': {}, '/': {}, '*': {}, }

oper = input("Виберіть операцію (+, -, *, /): ")


def filling_dict(oper):
    for i in range(2, 10):
        for j in range(2, 10):
            vol = eval(f"{i}{oper}{j}")
            dict_1[oper][i, j] = round(vol, 2)
    return dict_1


def table(dict_1):
    if oper in dict_1:
        for i in range(2, 10):
            print()
            print(end=" ")
            for j in range(2, 10):
                print(f"{i} {oper} {j} = {dict_1[oper][i, j]}\n", end=" ")


filling_dict(oper)
table(dict_1)
