# 2116_주사위쌓기_문제풀이
# 2022-02-18
import sys
sys.stdin = open('input.txt', 'r')


# 인덱스 기준
# 0 <-> 5
# 1 <-> 3
# 2 <-> 4
def dice(idx):
    if idx == 0:
        return 5
    elif idx == 1:
        return 3
    elif idx == 2:
        return 4
    elif idx == 3:
        return 1
    elif idx == 4:
        return 2
    else:
        return 0


# max 값은 두 인덱스 제외 맥스값
# 처음숫자 정할시 자동으로 나머지 완성
N = int(input())


num_arr = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0
# 경우의수는 총 6가지
for i in range(6):
    now_sum = 0
    bottom_idx = i
    for j in range(N):
        top_idx = dice(bottom_idx)
        # 2개를 제외한 나머지중 최대값
        max_num = 0
        for k in range(6):
            if k == top_idx or k == bottom_idx:
                continue
            else:
                if num_arr[j][k] > max_num:
                    max_num = num_arr[j][k]
        # now_sum 에 최대값 더하기
        now_sum += max_num
        # top_num 와 동일한 다음 주사위 bottom num 인덱스 구하기
        if j == N-1:
            break
        for h in range(6):
            if num_arr[j+1][h] == num_arr[j][top_idx]:
                # top_idx 를 bottom_idx 로 변경하여 다시 시작
                bottom_idx = h

    if now_sum > max_sum:
        max_sum = now_sum

print(max_sum)


