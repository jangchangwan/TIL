# 10815_숫자 게임
# 2022-06-29
# 이분탐색 + 정렬

def search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if N_lst[mid] == target:
            return 1
        elif N_lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


N = int(input())
N_lst = list(map(int, input().split()))

M = int(input())
M_lst = list(map(int, input().split()))

N_lst.sort()

answer = []
for m in M_lst:
    if search(m, 0, N-1):
        answer.append(1)
    else:
        answer.append(0)

print(*answer)
