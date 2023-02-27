# 수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.

# 즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.

# 입력
# 첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)

# 둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)

# 출력
# 첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.

# 예제 입력 1 
# 5 3
# 1 2 3 1 2
# 예제 출력 1 
# 7

n, m = map(int, input().split())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
 
remainder_info = [0 for _ in range(m)]
remainder_info[0] = 1
 
total = 0
for i in range(n):
    total += num_list[i]
    r = total % m
    # 나머지 값에 따라서 idx 정보 저장
    remainder_info[r] += 1

count = 0
for i in remainder_info:
    count += i*(i - 1) // 2
 
print(count)

def Back_T(total, idx):
    global cnt
    if idx == N:
        return
    
    total += N_list[idx]
    Back_T(total, idx+1)
    if total % M == 0:
        cnt += 1
    total -= N_list[idx]

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
cnt = 0
Back_T(0, 0)

print(cnt)