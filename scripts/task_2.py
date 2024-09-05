"""
Задача 2:
Имеется массив целых чисел, удалите наименьшее значение. Не изменяйте исходный массив/список. Если есть несколько
элементов с одинаковым значением, удалите тот, у которого индекс ниже. Если вы получаете пустой массив/список,
верните пустой массив/список.
Не меняйте порядок оставшихся элементов.
Пример:
* Input: [1,2,3,4,5], output = [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]

"""
def remove_small_number(numbers):
    # Проверка на пустой список
    if not numbers:
        return []

    # Находим наименьшее значение
    min_value = min(numbers)

    # Находим индекс первого вхождения наименьшего значения
    min_index = numbers.index(min_value)

    # Создаем новый список, исключая элемент с найденным индексом
    result = numbers[:min_index] + numbers[min_index + 1:]

    return result

if __name__ == "__main__":
    print(remove_small_number([1, 2, 3, 4, 5]))
    print(remove_small_number([5, 3, 2, 1, 4]))
    print(remove_small_number([2, 2, 1, 2, 1]))
    print(remove_small_number([]))
