def validate(hand):
    return 0 <= hand <= 2

def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

def judge(player, computer):
    if player == computer:
        return '引き分け'
    elif player == 0 and computer == 1:
        return '勝ち'
    elif player == 1 and computer == 2:
        return '勝ち'
    elif player == 2 and computer == 0:
        return '勝ち'
    else:
        return '負け'

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')

while True:
    try:
        print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
        player_hand = int(input('数字で入力してください：'))
        if validate(player_hand):
            break
        else:
            print('0、1、または2を入力してください。')
    except ValueError:
        print('数字で入力してください。')

computer_hand = 1
print_hand(player_hand, player_name or 'ゲスト')
print_hand(computer_hand, 'コンピューター')

result = judge(player_hand, computer_hand)
print('結果は' + result + 'でした')
