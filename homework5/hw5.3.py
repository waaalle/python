"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.

"""
summa = 0
count = 0
persons = []
with open('test_3.txt', 'r') as file_obj:
    for line in file_obj:
        print(line, end='')
        tokens = line.split(':')
        if int(tokens[1]) <= 20:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f'\npersons: {persons}')
print(f'average: {result}')
