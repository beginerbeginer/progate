items = {'apple': 100, 'banana': 200, 'orange': 400}
total_price = 0

for item_name in items:
    print('--------------------------------------------------')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')

    while True:
        try:
            input_count = input('購入する' + item_name + 'の個数を入力してください:')
            count = int(input_count)
            
            if count < 0:
                print('エラー：個数は0以上の数値を入力してください。')
                continue
            break
        except ValueError:
            print('エラー：個数は数値で入力してください。')
        
    print('購入する' + item_name + 'の個数は' + input_count + '個です')
    item_total_price = items[item_name]*count
    total_price += item_total_price
print('支払い金額は' + str(total_price) + '円です')
