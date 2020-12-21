"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.

"""

name = input('Enter your name')
surname = input('Enter your surname')
year = input('Enter your birth year')
city = input('Enter your city')
mail = input('Enter your email')
phone = input('Enter your phone')


def my_func():
    return ' '.join([name, surname, year, city, mail, phone])


print(my_func())
