# 1219_길찾기_문제풀이
# 2022-02-22

import sys
sys.stdin = open('input.txt', 'r')

T = 10

for t in range(1, T+1):
    N, E = map(int, input().split())
    total_list = [[] for _ in range(100)]
    # 경로 받아오기
    root_lst = list(map(int, input().split()))
    # E 만큼 반복
    for e in range(E):
        # 뒤에서부터 경로 받아오기
        end = root_lst.pop()
        start = root_lst.pop()
        total_list[start].append(end)

    result = []
    i = 0
    while i != len(result) or len(result) == 0:
        # 처음 경로가 없을경우 더이상 찾지말고 나온다.
        if len(total_list[0]) == 0:
            break
        # 초기값은 바로 더해준다.
        elif len(result) == 0:
            result += total_list[0]
            continue

        t_storage = total_list[result[i]]
        for j in t_storage:
            # 중복 피하기
            if j in result:
                continue
            result += [j]
        i += 1
    # 경로 안에 있을경우
    if 99 in result:
        ans = 1
    # 경로 안에 없을 경우
    else:
        ans = 0

    print('#{} {}'.format(t, ans))