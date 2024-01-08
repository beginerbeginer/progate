import utils

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：') or 'ゲスト'

while True:
    try:
        print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
        player_hand = int(input('数字で入力してください：'))
        if utils.validate(player_hand):
            break
        else:
            print('0、1、または2を入力してください。')
    except ValueError:
        print('数字で入力してください')

computer_hand = 1
if player_name == '':
    utils.print_hand(player_hand)
else:
    utils.print_hand(player_hand, player_name)
utils.print_hand(computer_hand, 'コンピュータ')

result = utils.judge(player_hand, computer_hand)
print('結果は' + result + 'でした')
