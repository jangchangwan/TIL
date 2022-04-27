# 14939_불 끄기_문제풀이
# 2022-04-27
# PyPy3 117276 KB / 224 ms
from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')



'''
데이터가 # , O 만 존재하므로 True, False로 데이터로 변경하고
한줄당 on / off  10번 할수 있으모르 2^10 = 1024가지의 경우의수가 있고
1. 경우의 수에 대한 전구를 세팅하고
2. 두번째 줄부터 배열을 순회하며 한칸위에 전구가 켜져있으면 해당위치에서 전구를 누른다.
3. 마지막줄 확인후 체크 성공
4. 최소 값 비교해서 최소값 출력
'''


# 버튼 누르기
def press(arr, r, c):
    for d in range(5):
        nr = r + dr[d]
        nc = c + dc[d]
        if (0 <= nr < 10) and (0 <= nc < 10):
            arr[nr][nc] = (arr[nr][nc] + 1) % 2


dr = [-1, 1, 0, 0, 0]
dc = [0, 0, 0, -1, 1]

arr = [list(map(str, input())) for _ in range(10)]
bit = [[False] * 10 for _ in range(10)]

ans = int(1e9)
for i in range(10):
    for j in range(10):
        if arr[i][j] == 'O':
            bit[i][j] = True


for case in range(1 << 10):
    temp = [bit[i][:] for i in range(10)]
    cnt = 0
    mask = 1
    # 첫번째 줄에 나올 수 있는 스위치 경우의 수 만들기
    for j in range(9, -1, -1):
        if case & mask:
            press(temp, 0, j)
            cnt += 1
        mask <<= 1

    # 두 번째 줄부터 끝까지 반복
    for i in range(1, 10):
        for j in range(10):
            # 현재 위치위의 전구가 켜져있는 경우
            if temp[i-1][j]:
                press(temp, i, j)
                cnt += 1

    # 마지막줄 전구가 다꺼져있을경우 성공
    if sum(temp[9]) == 0:
        ans = min(ans, cnt)

print(ans)