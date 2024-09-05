"""
Этот файл создает тестовую базу данных SQLite и заполняет её тестовыми данными с помощью библиотеки Faker.

"""

import random
from faker import Faker
import sqlite3

# Инициализация Faker и соединения с базой данных SQLite
faker = Faker()
conn = sqlite3.connect('test_database.db') # Название создаваемой базы
cursor = conn.cursor()

# Количество департаментов
departament = 40
# Количество сотрудников
employee = 300

# Создаем таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS DEPARTAMENT (
    ID INTEGER PRIMARY KEY,
    NAME TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS EMPLOYEE (
    ID INTEGER PRIMARY KEY,
    DEPARTAMENT_ID INTEGER,
    CHIEF_ID INTEGER,
    NAME TEXT,
    SALARY REAL,
    FOREIGN KEY (DEPARTAMENT_ID) REFERENCES DEPARTAMENT(ID),
    FOREIGN KEY (CHIEF_ID) REFERENCES EMPLOYEE(ID)
)
''')

# Вставка тестовых данных в таблицу DEPARTAMENT
departament_names = [faker.company() for _ in range(departament)]

for idx, name in enumerate(departament_names, start=1):
    cursor.execute('INSERT INTO DEPARTAMENT (ID, NAME) VALUES (?, ?)', (idx, name))


# Вставка тестовых данных в таблицу EMPLOYEE
employee_data = []

for i in range(1, employee + 1):
    print('Создано записей: ', i, ' из ', employee)
    departament_id = random.randint(1, len(departament_names))
    chief_id = random.choice([None] + employee_data)
    name = faker.name()
    salary = round(random.uniform(30000, 120000), 2) # Интервал зарплат

    cursor.execute('''
        INSERT INTO EMPLOYEE (ID, DEPARTAMENT_ID, CHIEF_ID, NAME, SALARY)
        VALUES (?, ?, ?, ?, ?)
    ''', (i, departament_id, chief_id, name, salary))

    employee_data.append(i)

# Сохранение данных и закрытие соединения
conn.commit()
conn.close()

print("Тестовые данные успешно добавлены в базу данных.")