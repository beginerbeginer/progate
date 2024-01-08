money = 1000
items = {'apple': 100, 'banana': 200, 'orange': 400}

for item_name in items:
    print('--------------------------------------------------')
    print('財布には' + str(money) + '円入っています')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')

    while True:
        try:
            input_count = input('購入する' + item_name + 'の個数を入力してください:')
            count = int(input_count)

            if count < 0:
                print('エラー:個数は0以上の値を入力してください')
                continue

            total_price = items[item_name] * count

            if money >= total_price:
                print(item_name + 'を' + input_count + '個買いました')
                money -= total_price
            else:
                print('お金が足りません')
                print(item_name + 'を買えませんでした')
            break
        except ValueError:
            print('エラー:個数は数値で入力してください。')

    if money == 0:
        print('財布が空になりました')
        break

print('残金は' + str(money) + '円です')
