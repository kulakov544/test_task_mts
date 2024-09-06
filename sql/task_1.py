"""
Задание 1
Вывести список сотрудников, получающих заработную плату большую чем у непосредственного руководителя.
Написать запрос двумя способами

Решение:
Тестирование кода происходит на сгенерированной базе данных.
test_database.db с небольшим набором данных
test_database_big.db с миллионом сотрудников

Первый способ(query1)
В запросе к таблице присоединяется она же таким образом, чтобы присоединенная запись
соответствовала записи руководителя.

Второй способ(query2)
В запросе делается подзапрос, который находит роководителя зарплата которого
меньше чем у сотрудника. Если такой руководитель нашелся сотрудник будет добавлен в результат запроса.

"""

import sqlite3
from pathlib import Path


def query1(database_path: str | Path):
    """
    Функция отправляет запрос базе данных и печатает ответ
    :param database_path: Путь к базе данных
    """
    try:
        conn = sqlite3.connect(database_path)
    except Exception as e:
        print('Ошибка при подключении к базе данных: ', e)
    else:
        try:
            cursor = conn.cursor()

            # Запрос с использованием JOIN
            query = '''
            SELECT e1.NAME, e1.ID, e1.SALARY, e2.NAME, e2.SALARY
            FROM EMPLOYEE e1
            JOIN EMPLOYEE e2 ON e1.CHIEF_ID = e2.ID
            WHERE e1.SALARY > e2.SALARY;
            '''

            cursor.execute(query)
            results = cursor.fetchall()

            print("Сотрудники с зарплатой больше, чем у непосредственного руководителя (JOIN):")
            for row in results:
                print(f"Сотрудник: {row[0]}, ID: {row[1]}, Зарплата: {row[2]}, Начальник: {row[3]}, Зарплата начальника: {row[4]}")

            print('Найдено сотрудников: ', len(results))

        except Exception as e:
            print('ошибка при работе с базой данных: ', e)
        finally:
            conn.close()

def query2(database_path: str | Path):
    """
    Функция отправляет запрос базе данных и печатает ответ
    :param database_path: Путь к базе данных
    """
    try:
        conn = sqlite3.connect(database_path)
    except Exception as e:
        print('Ошибка при подключении к базе данных: ', e)
    else:
        try:
            cursor = conn.cursor()

            # Запрос с использованием EXISTS
            query = '''
            SELECT e1.ID, e1.NAME, e1.SALARY
            FROM EMPLOYEE e1
            WHERE EXISTS (
                SELECT 1
                FROM EMPLOYEE e2
                WHERE e2.ID = e1.CHIEF_ID
                  AND e1.SALARY > e2.SALARY
            );
            '''

            cursor.execute(query)
            results = cursor.fetchall()

            print("Сотрудники с зарплатой больше, чем у непосредственного руководителя (JOIN):")
            for row in results:
                print(
                    f"ID: {row[0]}, Имя: {row[1]}, Зарплата: {row[2]}")

            print('Найдено сотрудников: ', len(results))

        except Exception as e:
            print('ошибка при работе с базой данных: ', e)
        finally:
            conn.close()


if __name__ == "__main__":
    database_path = 'test_database.db'  # Укажите путь к вашей базе данных SQLite

    query1(database_path)
    #query2(database_path)

