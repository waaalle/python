goods = []
while input("Would you like add product? Enter yes/no: ") == 'yes':
    number = int(input("Enter product number: "))
    features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
    while input("Would you like add product parameters? Enter yes/no: ") == 'yes':
        feature_key = input("Enter feature product: ")
        feature_value = input("Enter feature value product: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analytics:
            analytics[feature_key].append(feature_value)
        else:
            analytics[feature_key] = [feature_value]
print(analytics)
