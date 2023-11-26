# ДЗ 7 Уроку
#
# Створіть два файли
# в 1-му напишіть такі функції:
# 1) сортування списка по зростанню числа, від меншого до більшого.
# Функція приймає список з чисел і повертає відсортований список.
# 2) сортування списка на спад, від  більшого до меншого.
# Функція приймає список з чисел і повертає відсортований список.
# 3) сортування за кількістю букв у слові.
# Функція приймає список з слів і повертає відсортований список.
#
# 2-ий файл з трьома тестами який буде тестити ці три функції. В кожному тесті 1 тест.
# В тестових функціях ми ставимо типізацію.
# В першому файлі в всіх функціях проставляємо що приймає і що повертає.
# Встановіть собі пайтест і прораньте.
# До домашки отрім кода додайте скріншот прогона тестів.



def sortUp (*args : tuple):
    catalog= list(args)
    return sorted(catalog)


def sortDown (*args : tuple):
    catalog = list(args)
    return sorted(catalog, reverse=True)

def sortLen (*args : tuple):
    catalog = list(args)
    return sorted(catalog, key=len)











