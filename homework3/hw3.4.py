"""
Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение
числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо
обойтись без встроенной функции возведения числа в степень.

"""


def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'Введите x положительный, а y отрицательный'
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            return f'the result is {round(result, 6)}'
    except ValueError:
        return 'enter only numbers'


number1 = input('введите действительное положительно число x')
number2 = input('введите целое отрицательное число y')
print(my_func(number1, number2))
