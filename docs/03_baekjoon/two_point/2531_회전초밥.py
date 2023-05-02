import sys
# N : 접시수
# D : 초밥 종류
# K : 연속으로 먹을 수 있는 접시수
# C : 쿠폰 
n, d, k, c = map(int, sys.stdin.readline().rsplit())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
left, right = 0, 0
answer = 0

while left != n:
    right = left + k
    case = set()
    addable = True
    for i in range(left, right):
        i %= n
        case.add(arr[i])
        if arr[i] == c: addable = False

    cnt = len(case)
    # 쿠폰 추가
    if addable: 
        cnt += 1
    answer = max(answer, cnt)
    left += 1

print(answer)