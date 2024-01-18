list = [num for num in range(34, 122) if num % 3 == 0 and num % 2 == 0]
print(list)


class Calc:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("На нуль ділити не можна!")

    @staticmethod
    def greet():
        print("Привіт, я калькулятор.")


import random

matrix = [[random.randint(0, 9) for _ in range(7)] for _ in range(7)]

for row in matrix:
    print(row)
