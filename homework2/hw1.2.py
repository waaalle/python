my_list = list(input('Enter numbers without using space'))
for ind in range(0, len(my_list) - 1, 2):
    my_list[ind], my_list[ind + 1] = my_list[ind + 1], my_list[ind]
print('Changed list is', my_list)
