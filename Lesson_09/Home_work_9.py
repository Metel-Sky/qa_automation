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

# 4) перепишіть декоратор який заміряє час з уроку в домашку,  ^-^
# можете його поклацати, як він працює



from datetime import datetime
def func_wrapper_time(func):
    def wrapper(*arg, **kwarg):
        start = datetime.now()
        result = func(*arg, **kwarg)
        delta_time = datetime.now() - start
        print("Час виконання функції : ", delta_time)
        return result
    return wrapper

import time
@func_wrapper_time
def foo_1(*arg, **kwarg):
    print("foo_1")
    time.sleep(2)


@func_wrapper_time
def foo_2(*arg, **kwarg):
    print("foo_2")
    time.sleep(1)

foo_1()
foo_2()