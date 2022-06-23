# 2110_공유기설치_문제풀이
# 2022-04-23


import sys
sys.stdin = open('input.txt', 'r')


# 범위가 0 ~ 1,000,000,000 이라 완전탐색을 할경우 시간초과가 뜰 것같다
# 이분탐색으로 풀면 시간을 줄일수 있을것이다.


N, C = map(int, input().split())

N_lst = [int(input()) for _ in range(N)]


# 정렬시켜준다.
N_lst.sort()
start = 1
end = N_lst[-1] - N_lst[0]
result = 0
while start <= end:
    cnt = 0
    mid = (start+end)//2
    for i in range(N):
        if i == 0:
            temp = N_lst[i]
            cnt += 1
        else:
            if N_lst[i] >= temp + mid:
                temp = N_lst[i]
                cnt += 1

    if cnt >= C:
        start = mid + 1
        if result < mid:
            result = mid
    else:
        end = mid - 1

print(result)