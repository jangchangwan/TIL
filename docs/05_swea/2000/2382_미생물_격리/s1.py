# 2382_미생물_격리_문제풀이
# 2022-03-23

import sys
sys.stdin = open('input.txt', 'r')

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N, time, K = map(int, input().split())
    microbe_lst = [list(map(int, input().split())) for _ in range(K)]
    base_arr = [[1] * N] + [([1]+[0]*(N-2)+[1]) for _ in range(N-2)] + [[1] * N]
    t = 0
    for _ in range(time):
        for k in range(K):
            i, j, cnt, dir = microbe_lst[k][0], microbe_lst[k][1], microbe_lst[k][2], microbe_lst[k][3]
            i += dx[dir-1]
            j += dy[dir-1]
            # 테두리에 걸릴 시
            if base_arr[i][j] == 1:
                cnt //= 2                   # 미생물을 절반으로
                if dir == 1 or dir == 3:    # 방향전환
                    dir += 1
                else:
                    dir -= 1
            microbe_lst[k] = [i, j, cnt, dir]

        # 겹치는거 합쳐주기
        for a in range(K):
            max_cnt = microbe_lst[a][2]
            max_dir = microbe_lst[a][3]
            sum_cnt = microbe_lst[a][2]

            for b in range(a+1, K):

                if (microbe_lst[a][0] == microbe_lst[b][0]) and (microbe_lst[a][1] == microbe_lst[b][1]):
                    if max_cnt < microbe_lst[b][2]:
                        sum_cnt += microbe_lst[b][2]
                        max_cnt = microbe_lst[b][2]
                        max_dir = microbe_lst[b][3]
                        microbe_lst[b][2] = 0
                    else:
                        sum_cnt += microbe_lst[b][2]
                        microbe_lst[b][2] = 0
            microbe_lst[a][2] = sum_cnt
            microbe_lst[a][3] = max_dir
        # 미생물 이 없을 경우 군집 없애기
        k = 0
        while k != len(microbe_lst):
            cnt = microbe_lst[k][2]

            if cnt == 0:
                microbe_lst.pop(k)
                continue
            k += 1
        K = len(microbe_lst)

    total_cnt = 0
    for k in range(K):
        total_cnt += microbe_lst[k][2]
    print('#{} {}'.format(tc, total_cnt))