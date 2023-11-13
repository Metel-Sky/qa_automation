

print("Для початку Введіть список товарів")
list_of_goods = [0]

goods_1 = input("Введіть назву товару: " )
list_of_goods.append(goods_1)

goods_2 = input("Введіть назву товару: " )
list_of_goods.append(goods_2)

goods_3 = input("Введіть назву товару: " )
list_of_goods.append(goods_3)

goods_4 = input("Введіть назву товару: " )
list_of_goods.append(goods_4)

goods_5 = input("Введіть назву товару: " )
list_of_goods.append(goods_5)
print(f"Товари в списку \n{list_of_goods[1]} \n{list_of_goods[2]}"
      f"\n{list_of_goods[3]} \n{list_of_goods[4] }\n{list_of_goods[5]}")
var = int(input("Введіть номер вже купленого товару: "))

list_of_goods.pop(var)
list_of_goods.pop(0)
print(list_of_goods)
list_of_goods= [0] + list_of_goods
var = int(input("Введіть номер вже купленого товару: "))
list_of_goods.pop(var)
list_of_goods.pop(0)
print(list_of_goods)
list_of_goods= [0] + list_of_goods
var = int(input("Введіть номер вже купленого товару: "))
list_of_goods.pop(var)
list_of_goods.pop(0)
print(list_of_goods)
list_of_goods= [0] + list_of_goods
var = int(input("Введіть номер вже купленого товару: "))
list_of_goods.pop(var)
list_of_goods.pop(0)
print(list_of_goods)
list_of_goods= [0] + list_of_goods
var = int(input("Введіть номер вже купленого товару: "))
list_of_goods.pop(var)
list_of_goods.pop(0)
print(list_of_goods)

if not list_of_goods:
      print("Ваш список закупок пустий!!!")
else:
      print(f"Ви ще не все купили {list_of_goods}")

list_2 = input("Створити новий список? Y\\N ")
if list_2.upper() =="Y":
      print("Для початку Введіть список товарів")
      list_of_goods = [0]

      goods_1 = input("Введіть назву товару: ")
      list_of_goods.append(goods_1)

      goods_2 = input("Введіть назву товару: ")
      list_of_goods.append(goods_2)

      goods_3 = input("Введіть назву товару: ")
      list_of_goods.append(goods_3)

      goods_4 = input("Введіть назву товару: ")
      list_of_goods.append(goods_4)

      goods_5 = input("Введіть назву товару: ")
      list_of_goods.append(goods_5)
      print(f"Товари в списку \n{list_of_goods[1]} \n{list_of_goods[2]}"
            f"\n{list_of_goods[3]} \n{list_of_goods[4]}\n{list_of_goods[5]}")
else:
      print("Гарного дня!!!")







