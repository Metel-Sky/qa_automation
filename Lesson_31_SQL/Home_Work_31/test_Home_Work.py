# -*- coding: utf-8 -*-
import sqlite3
import pytest

@pytest.fixture
def create_database():

    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

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


def test_car_name(create_database):
    conn = create_database
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM cars WHERE id=1")
    result = cursor.fetchone()

    assert result[0] == 'Toyota'

    conn.close()
#qqqqqqqqqqqqqqqq
