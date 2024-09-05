"""
Задание 4
Вывести список сотрудников, не имеющих назначенного руководителя, работающего в том же отделе.
Написать запрос двумя способами.

Первый способ:
К таблице сотрудников подключаем таблицу сотрудников, так чтобы в подключенной таблице были руководители
работающие в этом же отделе.
Убираем сотрудников у которых нашлись такие руководители.

Второй способ:
Получаем таблицу сотрудников у которых начальник работает в этом же отделе.
Выбираем тех сотрудников которых нет в полученной таблице.
"""
import sqlite3
from pathlib import Path


def query1(database_path: str | Path) -> list:
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

            # Первый запрос с LEFT JOIN
            query = '''
            SELECT e1.*
            FROM EMPLOYEE e1
            LEFT JOIN EMPLOYEE e2 ON e1.CHIEF_ID = e2.ID AND e1.DEPARTAMENT_ID = e2.DEPARTAMENT_ID
            WHERE e2.ID IS NULL;
            '''

            cursor.execute(query)
            results = cursor.fetchall()

            return results

        except Exception as e:
            print('ошибка при работе с базой данных: ', e)
        finally:
            conn.close()

def query2(database_path: str | Path) -> list:
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

            # Второй запрос с NOT EXISTS
            query = '''
                SELECT e1.*
                FROM EMPLOYEE e1
                WHERE NOT EXISTS (
                    SELECT 1
                    FROM EMPLOYEE e2
                    WHERE e1.CHIEF_ID = e2.ID AND e1.DEPARTAMENT_ID = e2.DEPARTAMENT_ID
                );
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
    employees = query1(database_path)
    #employees = query2(database_path)

    print("Сотрудники без назначенного руководителя в том же отделе (LEFT JOIN):")
    for employee in employees:
        print(f"Employee ID: {employee[0]}, Department ID: {employee[1]}, CHIEF ID: {employee[2]}, Имя: {employee[3]}, Зарплата: {employee[4]}")

