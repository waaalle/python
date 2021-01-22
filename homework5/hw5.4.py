"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

"""

translator = {'One': 'odin', 'Two': 'dva', 'Three': 'tri', 'Four': 'chetyre'}
my_list = []
result = []
try:
    with open('test_4_output.txt', 'r') as file_obj:
        for line in file_obj:
            tokens = line.split(' - ')
            print(tokens)
            if tokens[0] in translator:
                word = translator[tokens[0]]
                result.append(word + ' - ' + tokens[1])
        print(result)
except IOError:
    print('Произошла ошибка ввода-вывода!')

try:
    with open('test_4_input.txt', 'w') as file_input:
        file_input.writelines(result)
except IOError:
    print('Произошла ошибка ввода-вывода!')
