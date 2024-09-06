"""
Задание 3
Вывести список ID отделов, количество сотрудников в которых не превышает 3 человек.
При подсчете исключить начальников своего отдела.

Решение:
Находим список сотрудников у которых нет подчиненных в своем отделе(department_employees)
Подсчитываем количество таких сотрудников в каждом отделе и отбираем те где меньше 3 человек.(employees_count)
Получившееся группируем по DEPARTAMENT_ID
"""


import sqlite3
from pathlib import Path


def get_id_small_departments(database_path: str | Path) -> list:
    """
    Функция отправляет запрос базе данных и возвращает ответ.
    :param database_path: Путь к базе данных
    :return: список ID отделов в которых менее 3 человек не считая руководителей
    """
    try:
        conn = sqlite3.connect(database_path)
    except Exception as e:
        print('Ошибка при подключении к базе данных: ', e)
    else:
        try:
            cursor = conn.cursor()

            # Запрос для нахождения ID отделов, в которых количество сотрудников не превышает 3 человек, исключая начальников этих отделов
            query = '''
                SELECT e.DEPARTAMENT_ID, COUNT(e.ID) 
                FROM EMPLOYEE e
                LEFT JOIN EMPLOYEE e2 ON e.ID = e2.CHIEF_ID AND e.DEPARTAMENT_ID = e2.DEPARTAMENT_ID
                WHERE e2.ID IS NULL
                GROUP BY e.DEPARTAMENT_ID
                HAVING COUNT(e.ID) <= 3
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
    departments = get_id_small_departments(database_path)

    print("ID отделов, в которых количество сотрудников не превышает 3 (исключая начальников):")
    for department in departments:
        print(f"Department ID: {department[0]}, Количество сотрудников: {department[1]}")

