proceeds = int(input('Enter proceeds'))
cost = int(input('Enter cost'))
if proceeds < cost:
    print('Компания работает в убыток')
elif proceeds == cost:
    print('Компания работает в ноль')
else:
    print('Компания работает в прибыль')
    profitability = proceeds / cost
    print(f'Рентабельность выручки : {profitability:.2f}')
    numbers = int(input('How many people work?'))
    profitability_num = proceeds / numbers
    print(f'Прибыль фирмы в расчете на одного сотрудника : {profitability_num:.2f}')
