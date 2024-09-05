"""
Задание 5
Найти список ID отделов с максимальной суммарной зарплатой сотрудников.
Если в запросе будет использоваться одинаковый подзапрос больше одного раза, то из этого
подзапроса предварительно создать набор_данных (любой способ, with или временная таблица).
И в итоговом запросе использовать этот набор_данных.

Решение:
Создаем набор данных из таблицы EMPLOYEE с группировкой по DEPARTAMENT_ID и суммой SALARY
Из этого набора данных получаем DEPARTAMENT_ID такие что зарплата является максимальной в наборе данных.
В случае если таких отделов будет два или больше, они все будут выведены.
"""
import sqlite3
from pathlib import Path


def get_max_salary(database_path: str | Path) -> list:
    """
    Функция отправляет запрос базе данных и возвращает ответ.
    :param database_path: Путь к базе данных
    :return: ответ от базы данных
    """
    try:
        conn = sqlite3.connect(database_path)
    except Exception as e:
        print('Ошибка при подключении к базе данных: ', e)
    else:
        try:
            cursor = conn.cursor()

            # Запрос с использованием WITH
            query = '''
            with sum_salary as
            (select DEPARTAMENT_ID, sum(SALARY) AS SALARY
            from EMPLOYEE
            group by DEPARTAMENT_ID)
            select DEPARTAMENT_ID
            from sum_salary a
            where a.SALARY = (select max(SALARY) from sum_salary)
            '''

            cursor.execute(query)
            results = cursor.fetchall()

            return results

        except Exception as e:
            print('ошибка при работе с базой данных: ', e)
        finally:
            conn.close()

if __name__ == "__main__":
    database_path = 'test_database.db'  # Укажите путь к вашей базе данных
    departments = get_max_salary(database_path)

    print("ID отделов с максимальной суммарной зарплатой сотрудников:")
    for department in departments:
        print(f"Department ID: {department[0]}")
