"""
Задача 3:
Ваша задача состоит в том, чтобы написать функцию, которая увеличивает строку, чтобы создать новую строку.
Если строка уже заканчивается числом, это число должно быть увеличено на 1.
Если строка не заканчивается числом. к новой строке следует добавить цифру 1.
Пример:
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100

"""

def get_enlarged_string(string):
    # Если получили пустую строку
    if not string:
        return string + '1'
    # Если в конце нет числа
    if not string[-1].isdigit():
        return string + '1'

    # Получаем длину строки и начинаем перебор
    len_string = len(string)

    for i in range(1, len_string):
        # Находим в конце число. Если оно начинается не с 9 увеличиваем его на 1.
        # Если это 9 идем дальше пока не найдем другие числа.
        if string[-i].isdigit():
            if string[-i] != '9':
                return string[:-i] + str(int(string[-i:])+1)
        else:
            # Если при переборе закончились числа и пошли буквы прибавляем к найденному 1.
            return string[:-i+1] + str(int(string[-i+1:]) + 1)


if __name__ == "__main__":
    print(get_enlarged_string('foo'))
    print(get_enlarged_string('foobar23'))
    print(get_enlarged_string('foo0042'))
    print(get_enlarged_string('foo9'))
    print(get_enlarged_string('ывап0000999'))
