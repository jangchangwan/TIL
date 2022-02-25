# 2304_창고_다각형_문제풀이
# 2022-02-25
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
N_lst = list()
max_L = max_H = 0
for n in range(N):
    L, H = map(int, input().split())
    N_lst.append((L, H))
    # 제일 높은 H값과 그 위치 찾아내기
    if H > max_H:
        max_L = L
        max_H = H

print('최대높이, 그 때 좌표 ', max_H, max_L)
# 정렬
for i in range(N):
    for j in range(i, N):
        if N_lst[i][0] > N_lst[j][0]:
            N_lst[i], N_lst[j] = N_lst[j], N_lst[i]

print('정렬 한 후 리스트',N_lst)

ans = 0
k = 0
area = N_lst[0][1]
for i in range(N_lst[0][0], max_L):
    if i == N_lst[k][0]:
        if N_lst[k][1] > area:
            area = N_lst[k][1]
        k += 1
    ans += area
print('처음부터 절반까지 값 : ', ans)
print('맨 뒤 위치', N_lst[-1][0])
area = N_lst[-1][1]
k = N-1
for i in range(N_lst[-1][0], max_L, -1):
    if i == N_lst[k][0]:
        if N_lst[k][1] > area:
            area = N_lst[k][1]
        k += 1
    ans += area
ans += max_H
print('최종 값 : ', ans)