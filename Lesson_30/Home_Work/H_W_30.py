# -*- coding: utf-8 -*-
import random
import string


def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    chars = ""

    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    if not chars:
        print("Не вибрано жодного типу символів. Повертаю порожній пароль.")
        return ""

    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def main():
    length = int(input("Введіть довжину паролю: "))
    use_uppercase = input("Включити великі літери? (y/n): ").lower() == 'y'
    use_lowercase = input("Включити малі літери? (y/n): ").lower() == 'y'
    use_digits = input("Включити цифри? (y/n): ").lower() == 'так'
    use_special_chars = input("Включити спеціальні символи? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    print("Згенерований пароль:", password)


if __name__ == "__main__":
    main()
