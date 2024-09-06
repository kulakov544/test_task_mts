import time
from contextlib import redirect_stdout
from io import StringIO

from task_1 import query1, query2
from task_2 import max_salary
from task_3 import get_id_small_departments
from task_4 import query1 as query1_4, query2 as query2_4
from task_5 import get_max_salary


# Функция для измерения времени выполнения и затраченной памяти синхронных функций
def measure_performance(func, repetitions, *args, **kwargs):
    # Замер времени выполнения
    start_time = time.time()

    # Перенаправляем стандартный вывод в пустую строку, чтобы скрыть принты
    f = StringIO()
    with redirect_stdout(f):
        # Вызов функции несколько раз
        result = None
        for _ in range(repetitions):
            result = func(*args, **kwargs)

    # Замер времени окончания
    end_time = time.time()

    execution_time = end_time - start_time

    print(f"Время выполнения ({repetitions} раз): {execution_time:.6f} секунд")

    return result


input_data = "test_database_big.db"
repit = 10

print('Task 1, вариант 1:')
print('Входящие данные: ', input_data)
measure_performance(query1, repit, input_data)

print('Task 1, вариант 2:')
print('Входящие данные: ', input_data)
measure_performance(query2, repit, input_data)
print('______________________________________________________________________')


print('Task 2:')
print('Входящие данные: ', input_data)
measure_performance(max_salary, repit, input_data)
print('______________________________________________________________________')

print('Task 3:')
print('Входящие данные: ', input_data)
measure_performance(get_id_small_departments, repit, input_data)
print('______________________________________________________________________')

print('Task 4, вариант 1:')
print('Входящие данные: ', input_data)
measure_performance(query1_4, repit, input_data)

print('Task 4, вариант 2:')
print('Входящие данные: ', input_data)
measure_performance(query2_4, repit, input_data)
print('______________________________________________________________________')

print('Task 5:')
print('Входящие данные: ', input_data)
measure_performance(get_max_salary, repit, input_data)
print('______________________________________________________________________')

"""
input_data = "test_database.db"

Task 1, вариант 1:
Входящие данные:  test_database.db
Время выполнения (1000 раз): 0.579687 секунд
Task 1, вариант 2:
Входящие данные:  test_database.db
Время выполнения (1000 раз): 0.482961 секунд
______________________________________________________________________
Task 2:
Входящие данные:  test_database.db
Время выполнения (1000 раз): 0.410046 секунд
______________________________________________________________________
Task 3:
Входящие данные:  test_database.db
Время выполнения (1000 раз): 0.368997 секунд
______________________________________________________________________
Task 4, вариант 1:
Входящие данные:  test_database.db
Время выполнения (1000 раз): 0.398000 секунд
Task 4, вариант 2:
Входящие данные:  test_database.db
Время выполнения (1000 раз): 0.404518 секунд
______________________________________________________________________
Task 5:
Входящие данные:  test_database.db
Время выполнения (1000 раз): 0.249001 секунд
______________________________________________________________________


input_data = "test_database_big.db"

Task 1, вариант 1:
Входящие данные:  test_database_big.db
Время выполнения (10 раз): 34.561614 секунд
Task 1, вариант 2:
Входящие данные:  test_database_big.db
Время выполнения (10 раз): 32.575093 секунд
______________________________________________________________________
Task 2:
Входящие данные:  test_database_big.db
Время выполнения (10 раз): 3.801773 секунд
______________________________________________________________________
Task 3:
Входящие данные:  test_database_big.db
Время выполнения (10 раз): 37.448397 секунд
______________________________________________________________________
Task 4, вариант 1:
Входящие данные:  test_database_big.db
Время выполнения (10 раз): 32.013268 секунд
Task 4, вариант 2:
Входящие данные:  test_database_big.db
Время выполнения (10 раз): 31.754741 секунд
______________________________________________________________________
Task 5:
Входящие данные:  test_database_big.db
Время выполнения (10 раз): 2.253570 секунд
______________________________________________________________________
"""