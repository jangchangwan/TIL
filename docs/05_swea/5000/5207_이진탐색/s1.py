# 5207_이진탐색_문제풀이
# 2022-03-31

import sys
sys.stdin = open('input.txt', 'r')


def binary_research(s, e, m, x):
    global cnt
    # 찾을 경우
    if find_lst[x] == research_lst[m]:
        cnt += 1
    else:
        # 검색한값이 찾는값보다 클 경우
        if find_lst[x] < research_lst[m]:
            e = m - 1
            m = (s + e) // 2
            if find_lst[x] > research_lst[m]:
                binary_research(s, e, m, x)
            elif find_lst[x] == research_lst[m]:
                cnt += 1
        # 검색한값이 찾는값보다 작을 경우
        elif find_lst[x] > research_lst[m]:
            s = m + 1
            m = (s + e) // 2
            if find_lst[x] < research_lst[m]:
                binary_research(s, e, m, x)
            elif find_lst[x] == research_lst[m]:
                cnt += 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    research_lst = list(map(int, input().split()))
    find_lst = list(map(int, input().split()))

    research_lst.sort()
    start = 0
    end = N-1
    mid = (start + end) // 2
    cnt = 0
    for m in range(M):
        binary_research(start, end, mid, m)
    print('#{} {}'.format(tc, cnt))