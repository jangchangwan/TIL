import sys
sys.stdin = open('input.txt', 'r')

# 케이크 길이
L = int(input())
# 방청객 수
N = int(input())
# 케이크 길이 만큼 1인 리스트 생성
L_lst = [0] + [1] * L
# 가장 많이 받은 케이스 수와 그 방청객 번호 초기화
max_n = 0
max_cnt = 0
max_if_n = 0
max_if_cnt =0
for n in range(1, N+1):
    P, K = map(int, input().split())
    cnt = 0
    # 제일 많이 받을거라 기대되는 사람
    if (K-P) > max_if_cnt:
        max_if_cnt = (K-P)
        max_if_n = n
    for i in range(P, K+1):
        if L_lst[i] == 1:
            L_lst[i] = 0
            cnt += 1
    # 실제로 많이 받는 사람
    if cnt > max_cnt:
        max_n = n
        max_cnt = cnt

print(max_if_n)
print(max_n)

