import time
import tracemalloc

from task_1 import sort_str
from task_2 import remove_small_number
from task_3 import get_enlarged_string

# Функция для измерения времени выполнения и затраченной памяти
def measure_performance(func, repetitions, *args, **kwargs):
    # Замер времени выполнения
    start_time = time.time()

    # Запуск измерения памяти
    tracemalloc.start()

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

    print(f"Время выполнения (1000 раз): {execution_time:.6f} секунд")
    print(f"Использовано памяти: {used_memory:.6f} MB")

    return result


input_data = "is2 Thi1s T4est 3a"

print('Task 1:')
print('Входящие данные: ', input_data)
result = measure_performance(sort_str, 10000, input_data)
print("Результат последнего выполнения:", result)


input_data = [2, 2, 1, 2, 1]

print('Task 2:')
print('Входящие данные: ', input_data)
result = measure_performance(remove_small_number, 10000, input_data)
print("Результат последнего выполнения:", result)


input_data = 'foo099'

print('Task 3:')
print('Входящие данные: ', input_data)
result = measure_performance(get_enlarged_string, 10000, input_data)
print("Результат последнего выполнения:", result)