# 2805_나무자르기_문제풀이
# 2022-04-05
import sys
sys.stdin = open('input.txt', 'r')
# N : 나무수  M : 원하는 양
tree, M = map(int, input().split())
tree_lst = list(map(int, input().split()))


start = 1
end = max(tree_lst)

while start <= end:
    mid = (start + end) // 2

    log = 0
    for i in tree_lst:
        if i >= mid:
            log += i - mid
        if log > M:
            break
    # 많이 자른경우 높이를 올린다
    if log >= M:
        start = mid + 1
    # 적게 잘린경우 높이를 내린다.
    else:
        end = mid - 1
print(end)