# 1) додайте requirements.txt на ваш гіт   ^-^


# 2) Виберіть будь-яку помилку яка вам подобається і   ^-^
# зробіть функцію яка перевіряє на цю помилку
# (в функції try except)

# try:
#     print((aa))
# except NameError:
#     print("А тепер зітри все і напиши нормально!!!")

# 3) зробіть функцію як ми робили з додаванням тільки замість двох чисел,  ^-^
# зробіть три числа і протестуйте її всіма трьома методами

def add_thre_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = number_1 + number_2 + number_3
    return result

# 4) перепишіть декоратор який заміряє час з уроку в домашку,
# можете його поклацати, як він працює