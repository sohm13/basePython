"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i**2 for i in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(arr, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return [v for v in arr if v % 2 != 0]
    if filter_type == EVEN:
        return [v for v in arr if v % 2 == 0]
    if filter_type == PRIME:
        arr_res = []
        for v in arr:
            if v == 2:
                arr_res.append(v)
            elif v % 2 != 0 and v != 1:
                is_simple = True
                for i in range(2, v):
                    if v % i == 0:
                        is_simple = False
                        break
                if is_simple:
                    arr_res.append(v)
        return arr_res

