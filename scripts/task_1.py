"""
Задача 1:
Ваша задача - отсортировать заданную строку. Каждое слово в строке будет содержать одно число. Это число - позиция,
которую должно занимать слово в результате.
Примечание: Цифры могут быть от 1 до 9. Таким образом, 1 будет первым словом (а не 0).
Если входная строка пуста, верните пустую строку. Слова во входной строке будут содержать только допустимые последовательные числа.
Пример:
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"

"""
import re


def sort_str(str_for_sort):
    # Если строки нет возвращаем пустую строку
    if not str_for_sort:
        return ""

    word_dic = {}

    # Разделяем строку на слова
    words = str_for_sort.split()

    # Ищем в словах цифры и заполняем словарь word_dic используя цифры как ключи
    for word in words:
        match_number_in_word = re.search(r'\d', word)
        if match_number_in_word is None:
            return f"В слове {word} отсутствует число."

        number_in_word = match_number_in_word.group()
        word_dic[number_in_word] = word

    # Сортируем ключи словаря word_dic
    sorted_keys = sorted(word_dic)

    # Генерируем новую строку используя отсортированные ключи
    sort_string = ' '.join(word_dic[key] for key in sorted_keys)

    return sort_string

if __name__ == "__main__":
    str_1 = "is2 Thi1s T4est 3a"
    str_2 = "word word1 word1"

    print(str_2)
    print(sort_str(str_2))