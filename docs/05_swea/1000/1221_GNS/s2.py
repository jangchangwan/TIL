import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    # 필요없는 데이터라 _ 로 표기
    _ = input()
    number_map = {
                   "ZRO": 0,
                   "ONE": 1, "TWO": 2, "THR": 3,
                   "FOR": 4, "FIV": 5, "SIX": 6,
                   "SVN": 7, "EGT": 8, "NIN": 9,
                   }
    string = input().split()
    # print(string)
    string.sort(key=lambda num: number_map[num])
    print('#{} {}'.format(t, ' '.join(string)))
