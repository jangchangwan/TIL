# 1208_부분수열의 합2_문제풀이
# 2022-06-08

# 예상은 했지만 2 ^ 40 이므로 시간초과를 피할 수 없었다.

# 0을 기준으로 나누면  이분탐색으로 2 ^ 20으로 한다면 가능할 것같다

def DFS(idx, nums, total, subset):
    if idx == len(nums):
        subset[total] = subset.get(total, 0) + 1
        return
    DFS(idx+1, nums, total, subset)
    DFS(idx+1, nums, total + nums[idx], subset)


# 입력
N, S = map(int, input().split())
N_lst = list(map(int, input().split()))


middle = N // 2
# 2개로 쪼갠다
N_left = N_lst[:middle]
N_right = N_lst[middle:]
left_subset = {}
right_subset = {}


DFS(0, N_left, 0, left_subset)
DFS(0, N_right, 0, right_subset)

# 길이가 0인 부분 수열 제외하기
left_subset[0] -= 1
right_subset[0] -= 1

# 없을 경우 디폴트 값은 0으로
cnt = left_subset.get(S, 0) + right_subset.get(S, 0)

for left in left_subset:
    if S - left in right_subset:
        cnt += left_subset[left] * right_subset[S-left]

# 출력
print(cnt)