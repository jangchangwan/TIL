# 4408_자기_방으로_돌아가기_문제풀이
# 2022-02-18
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    room_cnt = [0]*401
    for n in range(N):
        start, end = map(int, input().split())
        # 정렬 할것
        if start > end:
            start, end = end, start
        # start 가 짝수 인 경우
        if start % 2 == 0:
            start -= 1
        # end 가 홀수 인 경우
        if end % 2 == 1:
            end += 1
        for i in range(start, end+1):
            room_cnt[i] += 1

    max_cnt = 0
    for j in room_cnt:
        if j > max_cnt:
            max_cnt = j
    ans = max_cnt
    print('#{} {}'.format(t, ans))