# 5203_베이비진_게임_문제풀이
# 2022-03-29
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    card_lst = list(map(int, input().split()))

    player_1 = [0] * 10
    player_2 = [0] * 10
    ans = 0
    for idx, card in enumerate(card_lst):
        if ans != 0:
            break
        # player 2
        if idx % 2:
            player_2[card] += 1
            cnt = 0
            for i in player_2:
                if i >= 3:
                    ans = 2
                    break
                if i != 0:
                    cnt += 1
                    if cnt >= 3:
                        ans = 2
                        break
                else:
                    cnt = 0

        # player 1
        else:
            player_1[card] += 1
            cnt = 0
            for i in player_1:
                if i >= 3:
                    ans = 1
                    break
                if i != 0:
                    cnt += 1
                    if cnt >= 3:
                        ans = 1
                        break
                else:
                    cnt = 0

    print('#{} {}'.format(tc, ans))