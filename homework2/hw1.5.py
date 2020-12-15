my_list = [7, 5, 3, 3, 2]
element = int(input('Enter new element'))
i = 0
for ind in my_list:
    if element <= ind:
        i += 1
my_list.insert(i, element)
print(my_list)
