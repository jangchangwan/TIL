# 4871_그래프_경로_문제풀이
# 2022-02-22

import sys
sys.stdin = open('input.txt', 'r')

# 시행횟수
T = int(input())


for t in range(1, T+1):
    # 총 길이 데이터
    V, E = map(int, input().split())
    total_list = [[] for _ in range(V+1)]
    for e in range(E):
        # 출발과 도착 데이터
        start, end = map(int, input().split())
        total_list[start].append(end)

    # 확인해야할 데이터
    check_A, check_B = map(int, input().split())
    result = []
    i = 0
    # 한번 찾을때마다 무조건 1개이상은 있을 것이므로  그리고 처음 결과값이 0이여서
    while i != len(result) or len(result) == 0:
        # 처음 경로가 없을경우 더이상 찾지말고 나온다.
        if len(total_list[check_A]) == 0:
            break
        # 초기값은 바로 더해준다.
        elif len(result) == 0:
            result += total_list[check_A]
            continue

        t_storage = total_list[result[i]]
        for j in t_storage:
            # 중복 피하기
            if j in result:
                continue
            result += [j]
        i += 1
    # 경로 안에 있을경우
    if check_B in result:
        ans = 1
    # 경로 안에 없을 경우
    else:
        ans = 0

    print('#{} {}'.format(t, ans))