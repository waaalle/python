"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль.

"""


def div():
    try:
        arg1 = int(input('Input dividend'))
        arg2 = int(input('Input divider'))
        res = arg1 / arg2
    except ZeroDivisionError:
        return 'Wrong! You cannot use zero'

    return res


print(div())
