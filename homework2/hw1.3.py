seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
season_num = int(input('Enter seasons number from 1 to 12'))
if season_num == 12 or season_num == 1 or season_num == 2:
    print('The season is', seasons_list[0])
    print('The season is', seasons_dict.get(1))
elif season_num == 3 or season_num == 4 or season_num == 5:
    print('The season is', seasons_list[1])
    print('The season is', seasons_dict.get(2))
elif season_num == 6 or season_num == 7 or season_num == 8:
    print('The season is', seasons_list[2])
    print('The season is', seasons_dict.get(3))
else:
    print('The season is', seasons_list[3])
    print('The season is', seasons_dict.get(4))
