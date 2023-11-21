# Зробіть словник де буде табличка множення,
# додавання, ділення, і віднімання, чисел від 2 до 9(включно).
# Так як робили на уроці.
# Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
#
# Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити
# (додавання, віднімання, множення, ділення). і виведіть йому цю табличку.


dict_1 = {
    '+': {}, '-': {}, '/': {}, '*': {},
}

for i in range(2, 10):
    for j in range(2, 10):
        volume = j * i
        dict_1["*"][(i, j)] = volume



for i in range(2, 10):
    for j in range(2, 10):
        volume = j / i
        dict_1["/"][(i, j)] = volume

for i in range(2, 10):
    for j in range(2, 10):
        volume = j + i
        dict_1["+"][(i, j)] = volume

for i in range(2, 10):
    for j in range(2, 10):
        volume = j - i
        dict_1["-"][(i, j)] = volume

operation = input("Виберіть операцію (+, -, *, /): ")
if operation in dict_1:
    for i in range(2, 10):
        print()
        print(end=" ")
        for j in range(2, 10):
            print(f"{i} {operation} {j} = {dict_1[operation][i, j]}\n", end=" ")
