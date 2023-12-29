import pytest


def add_three_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = number_1 + number_2 + number_3
    with open("log.txt", "a") as file:
        file.write(f"\n{number_1}, {number_2}, {number_3} => {result}\n")
    return result

# with open("log.txt", "a") as file:
#     file.write(f"\n{number_1}, {number_2}, {number_3} => {result}\n")



