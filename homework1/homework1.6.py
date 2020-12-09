first_day = int(input('first_day'))
last_day = int(input('last_day'))
day = 0
while first_day < last_day:
    first_day = first_day * 1.1
    day = day + 1
    if first_day >= last_day:
        print(f'The result day is {day}')
