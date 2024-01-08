def is_valid_hand(hand):
    return 0 <= hand <= 2

def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')

try:
    player_hand = int(input('数字で入力してください：'))
    if is_valid_hand(player_hand):
        computer_hand = 1
        print_hand(player_hand, player_name or 'ゲスト')
        print_hand(computer_hand, 'コンピューター')
    else:
        print('正しい数値を入力してください')
except ValueError:
    print('数値で入力してください')
