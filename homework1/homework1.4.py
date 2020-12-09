number = int(input('Enter number'))
max_num = 0
while number > 10:
    num_1 = number % 10
    number = number // 10
    if num_1 > max_num:
        max_num = num_1
print(f'Max number is {max_num}')
