import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    day = input()
    day_dic = {'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1, 'SUN': 7}
    ans = day_dic[day]
    print('#{} {}'.format(tc, ans))