"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.

"""


def summary():
    try:
        with open('test_5.txt', 'w+') as file_obj:
            line = input('Enter numbers with space \n')
            file_obj.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print('Произошла ошибка ввода-вывода!')
    except ValueError:
        print('Неправильно набран номер. Произошла ошибка ввода-вывода!')


summary()
