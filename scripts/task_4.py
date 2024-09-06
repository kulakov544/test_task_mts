"""
Задача 4 (Для языка JavaScript):
Имеются 2 функции которые выполняются асинхронно. С использованием Promise и/или Asinc/Await реализовать вывод в консоль:
- Суммарный результат обеих функций.
- Последовательный вывод сначала 1 функции затем 2 в независимости от времени выполнения обеих функций (даже если 1я функция выполняется дольше 2й)


Я ранее не изучал JavaScript по этому решил задачу на Python.
При необходимости могу изучить JavaScript
"""
import asyncio

async def F1():
    await asyncio.sleep(2)  # Задержка в 2 секунды
    return "Result1"

async def F2():
    await asyncio.sleep(1)  # Задержка в 1 секунду
    return "Result2"

async def main():
    # Объединение результатов
    result1, result2 = await asyncio.gather(F1(), F2())  # Получим "Result1Result2"
    print(result1 + result2)

    # Поочередный вывод
    task1 = asyncio.create_task(F1())
    task2 = asyncio.create_task(F2())

    # Запускаем задачи и смотрим какая завершилась первой
    done, pending = await asyncio.wait([task1, task2], return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        print(task.result())

    # Ожидаем завершения оставшейся задачи
    done, pending = await asyncio.wait(pending)
    for task in done:
        print(task.result())

# Запуск асинхронной программы
asyncio.run(main())