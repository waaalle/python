my_list = [2, 5.6, 'word', True, [1, 25, 'abc'], (5, 6), {1: 'first', 2: 'second'}]
for ind, symbol in enumerate(my_list):
    print(f'{ind}. {symbol} is {type(symbol)}')
