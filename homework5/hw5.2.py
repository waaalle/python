"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.

"""
my_list = open('test_2.txt', 'r')
content = my_list.readlines()
print(f'String count is {len(content)}')
for i in range(len(content)):
    print(f'{len(content[i])} letters in {i + 1} line')
my_list = open('test_2.txt', 'r')
content = my_list.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_list.close()
