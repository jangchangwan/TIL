# 입력
N, K = map(int, input().split())
N_lst = list(input())

# 초기화
count = 0

for n in range(N):
    # 사람인 경우
    if N_lst[n] == 'P':
        for i in range(max(n-K, 0), min(n+K+1, N)):
            # 햄버거인 경우
            if N_lst[i] == 'H':
                N_lst[i] = 0
                count += 1
                break

# 출력  
print(count)
