"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.

"""


def my_func(x, y, z):
    sequence = [x, y, z]
    sequence.remove(min(sequence))
    return sum(sequence)


print(my_func(-7, 16, 5))
