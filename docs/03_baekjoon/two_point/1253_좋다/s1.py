# 1253_좋다_문제풀이
# 2022-06-24
# Python 3 / 1544ms
# 투 포인트 / 정렬

import sys
sys.stdin =open('input.txt', 'r')

# 입력
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
for i in range(N):
    # 탐색할 수를 제외한 리스트를 만든다.
    temp = arr[:i] + arr[i+1:]
    start, end = 0, len(temp) - 1

    while start < end:
        total = temp[start] + temp[end]
        # 탐색한 수이 있을경우
        if total == arr[i]:
            cnt += 1
            break
        elif total < arr[i]:
            start += 1
        else:
            end -= 1

print(cnt)