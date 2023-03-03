
# 입력
N = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()
X = int(input())

# 값 초기화
cnt = 0
i, j = 0, 1

# 동작
left, right = 0, N-1 # 왼쪽, 오른쪽
while left < right:
    temp = n_lst[left] + n_lst[right]
    if temp == X:
        cnt += 1
        left += 1
    elif temp < X:
        left += 1
    else:
        right -= 1


# 출력
print(cnt)