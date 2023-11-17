print("Для початку Введіть список товарів мінімум 5 ")
list_of_goods = input("Введіть ваші продукти через пробіл: ").split()


print(f"Товари в списку {list_of_goods}")
var = int(input("Введіть номер вже купленого товару: "))
list_of_goods.pop(var -1)
print(list_of_goods)

var = int(input("Введіть номер вже купленого товару: "))
list_of_goods.pop(var -1)
print(list_of_goods)

var = int(input("Введіть номер вже купленого товару: "))
list_of_goods.pop(var -1)
print(list_of_goods)

var = int(input("Введіть номер вже купленого товару: "))

list_of_goods.pop(var -1)
print(list_of_goods)

var = int(input("Введіть номер вже купленого товару: "))

list_of_goods.pop(var -1)
print(list_of_goods)


if not list_of_goods:
    print("Ваш список закупок пустий!!!")
else:
    print(f"Ви ще не все купили {list_of_goods}")

list_2 = input("Створити новий список? Y\\N ")
if list_2.upper() == "Y":
    list_of_goods = input("Введіть ваші продукти через пробіл: ").split()
    print(list_of_goods)
else:
    print("Гарного дня!!!")
