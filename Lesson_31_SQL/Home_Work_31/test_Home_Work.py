import sqlite3
import pytest

# Գ������ ��� ��������� �� ���������� ���� �����
@pytest.fixture
def create_database():
    # ϳ��������� �� ���� ����� (����������� �����������, ���� �� ����)
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # ��������� ������� "cars" � ��������� "id", "name", "model", "year"
    cursor.execute('''
        CREATE TABLE cars (
            id INTEGER PRIMARY KEY,
            name TEXT,
            model TEXT,
            year INTEGER
        )
    ''')

    # ��������� �������� ������
    cursor.execute("INSERT INTO cars (name, model, year) VALUES ('Toyota', 'Camry', 2022)")
    cursor.execute("INSERT INTO cars (name, model, year) VALUES ('Honda', 'Civic', 2021)")
    cursor.execute("INSERT INTO cars (name, model, year) VALUES ('Ford', 'Mustang', 2020)")

    # ���������� ��� �� �������� �'�������
    conn.commit()
    return conn

# ���� ��� �������� ���� "name"
def test_car_name(create_database):
    # ϳ��������� �� ���� �����
    conn = create_database
    cursor = conn.cursor()

    # ������ ������� � ���� "name" ������� "cars"
    cursor.execute("SELECT name FROM cars WHERE id=1")
    result = cursor.fetchone()

    # ��������, �� ���� "name" �� ��������� ��������
    assert result[0] == 'Toyota'

    # �������� �'�������
    conn.close()

