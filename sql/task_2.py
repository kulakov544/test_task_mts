"""
Задание 2
Вывести список сотрудников, получающих максимальную заработную плату в своем отделе.
К этому списку сотрудников добавить в вывод еще одно поле – средняя ЗП в отделе.

Делаем подзапрос к таблице EMPLOYEE. В нем делаем группировку по отделам и получаем
максимальную зарплату и среднюю зарплату по отделу.
Присоединяем этот подзапрос к таблице EMPLOYEE по ключу DEPARTAMENT_ID, так что-бы в
вывод попали только записи с максимальной зарплатой по отделу.
"""
import sqlite3
from pathlib import Path


def max_salary(database_path: str | Path) -> list:
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

            # Запрос для нахождения сотрудников с максимальной зарплатой в отделе и средней зарплаты отдела
            query = '''
            SELECT e.DEPARTAMENT_ID, e.NAME, e.SALARY, avg_salaries.avg_salary
            FROM EMPLOYEE e
            JOIN (
                SELECT DEPARTAMENT_ID, MAX(SALARY) AS max_salary, AVG(SALARY) AS avg_salary
                FROM EMPLOYEE
                GROUP BY DEPARTAMENT_ID
            ) AS avg_salaries
            ON e.DEPARTAMENT_ID = avg_salaries.DEPARTAMENT_ID AND e.SALARY = avg_salaries.max_salary
            ORDER BY e.DEPARTAMENT_ID;
            '''

            cursor.execute(query)
            results = cursor.fetchall()
            return results

        except Exception as e:
            print('ошибка при работе с базой данных: ', e)
        finally:
            conn.close()


if __name__ == "__main__":
    database_path = 'test_database_big.db'  # путь к базе данных
    employees = max_salary(database_path)

    print("Сотрудники с максимальной зарплатой в своем отделе и средняя зарплата в отделе:")
    for employee in employees:
        print(f"DEPARTAMENT_ID: {employee[0]}, Имя: {employee[1]}, Зарплата: {employee[2]}, "
              f"Средняя зарплата по департаменту: {round(employee[3], 2)}")
