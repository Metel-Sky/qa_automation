# #
# # math_tables = {
# #     '+': {},
# #     '-': {},
# #     '*': {},
# #     '/': {}
# # }
# #
# # # Заповнення таблички додавання
# # for i in range(2, 10):
# #     for j in range(2, 10):
# #         math_tables['+'][(i, j)] = i + j
# #
# # # Заповнення таблички віднімання
# # for i in range(2, 10):
# #     for j in range(2, 10):
# #         math_tables['-'][(i, j)] = i - j
# #
# # # Заповнення таблички множення
# # for i in range(2, 10):
# #     for j in range(2, 10):
# #         math_tables['*'][(i, j)] = i * j
# #
# # # Заповнення таблички ділення
# # for i in range(2, 10):
# #     for j in range(2, 10):
# #         math_tables['/'][(i, j)] = i / j
# #
# # # Запит користувача
# # operation = input("Виберіть операцію (+, -, *, /): ")
# #
# # # Перевірка чи операція валідна
# # if operation in math_tables:
# #     # Вивід таблички для обраної операції
# #     print(f"\nТабличка {operation}:\n")
# #     for i in range(2, 10):
# #         row = ""
# #         for j in range(2, 10):
# #             row += f"{math_tables[operation][(i, j)]}"
# #         print(row,"\n")
# # else:
# #     print("Невірна операція. Будь ласка, виберіть правильну операцію (+, -, *, /).")
# #
# #
# dict_1 = {
#     '+': {}, '-': {}, '/': {}, '*': {},
# }
#
# for i in range(2, 10):
#     for j in range(2, 10):
#         volume = j * i
#         dict_1["*"][(i, j)] = volume
#
# for i in range(2, 10):
#     for j in range(2, 10):
#         volume = j / i
#         dict_1["/"][(i, j)] = volume
#
# for i in range(2, 10):
#     for j in range(2, 10):
#         volume = j + i
#         dict_1["+"][(i, j)] = volume
#
# for i in range(2, 10):
#     for j in range(2, 10):
#         volume = j - i
#         dict_1["-"][(i, j)] = volume
#
#
#
# def math_table():
#     operation = input("Виберіть операцію (+, -, *, /): ")
#     if operation in dict_1:
#         for i in range(2, 10):
#             print()
#             print(end=" ")
#             for j in range(2, 10):
#                 print(f"{i} {operation} {j} = {dict_1[operation][i, j]}\n", end=" ")
#
#
# math_table()


# from win10toast import (ToastNotifier)
# import time
#
# toaster = ToastNotifier()
#
# while True:
#     toaster.show_toast("Повідомлення", "Пройшло 10 секунд", duration=10)
#     time.sleep(10)


import time
import ctypes


while True:
    ctypes.windll.user32.MessageBoxW(0, "Нагадування", "Пройшло 10 секунд", 0x40)
    time.sleep(10)