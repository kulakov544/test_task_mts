import time
import tracemalloc
from contextlib import redirect_stdout
from io import StringIO

from task_1 import query1, query2
from task_2 import max_salary
from task_3 import get_id_small_departments
from task_4 import query1, query2


# Функция для измерения времени выполнения и затраченной памяти синхронных функций
def measure_performance(func, repetitions, *args, **kwargs):
    # Замер времени выполнения
    start_time = time.time()

    # Запуск измерения памяти
    tracemalloc.start()

    # Перенаправляем стандартный вывод в пустую строку, чтобы скрыть принты
    f = StringIO()
    with redirect_stdout(f):
        # Вызов функции несколько раз
        result = None
        for _ in range(repetitions):
            result = func(*args, **kwargs)

    # Остановка измерения памяти
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Замер времени окончания
    end_time = time.time()

    execution_time = end_time - start_time
    used_memory = peak / 10**6  # Пиковое потребление памяти в мегабайтах

    print(f"Время выполнения ({repetitions} раз): {execution_time:.6f} секунд")
    print(f"Использовано памяти: {used_memory:.6f} MB")

    return result


input_data = "test_database.db"

print('Task 1, вариант 1:')
print('Входящие данные: ', input_data)
measure_performance(query1, 1000, input_data)


print('Task 1, вариант 2:')
print('Входящие данные: ', input_data)
measure_performance(query2, 1000, input_data)


print('Task 2:')
print('Входящие данные: ', input_data)
measure_performance(max_salary, 1000, input_data)

print('Task 3:')
print('Входящие данные: ', input_data)
measure_performance(get_id_small_departments, 1000, input_data)