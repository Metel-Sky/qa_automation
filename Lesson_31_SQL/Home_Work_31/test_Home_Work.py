import sqlite3
import pytest

# Фікстура для створення та заповнення бази даних
@pytest.fixture
def create_database():
    # Підключення до бази даних (створюється автоматично, якщо не існує)
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Створення таблиці "cars" з колонками "id", "name", "model", "year"
    cursor.execute('''
        CREATE TABLE cars (
            id INTEGER PRIMARY KEY,
            name TEXT,
            model TEXT,
            year INTEGER
        )
    ''')

    # Додавання декількох записів
    cursor.execute("INSERT INTO cars (name, model, year) VALUES ('Toyota', 'Camry', 2022)")
    cursor.execute("INSERT INTO cars (name, model, year) VALUES ('Honda', 'Civic', 2021)")
    cursor.execute("INSERT INTO cars (name, model, year) VALUES ('Ford', 'Mustang', 2020)")

    # Збереження змін та закриття з'єднання
    conn.commit()
    return conn

# Тест для перевірки поля "name"
def test_car_name(create_database):
    # Підключення до бази даних
    conn = create_database
    cursor = conn.cursor()

    # Вибірка значень з поля "name" таблиці "cars"
    cursor.execute("SELECT name FROM cars WHERE id=1")
    result = cursor.fetchone()

    # Перевірка, чи поле "name" має очікуване значення
    assert result[0] == 'Toyota'

    # Закриття з'єднання
    conn.close()

