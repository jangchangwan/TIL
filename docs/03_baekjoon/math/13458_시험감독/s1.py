# 13458_시험 감독_문제풀이
# 2022-03-22
import sys
sys.stdin = open('input.txt', 'r')

# 시험장 수
N = int(input())
# 각 시험장의 응시자 수
A_lst = list(map(int, input().split()))
# 총 감독관 , 부 감독관이 감시가능한 응시자수
B, C = map(int, input().split())

total_ans = 0
for A in A_lst:
    ans = 0
    # 총감독관은 무조건 한명만 있을수 있으므로
    temp = A - B
    ans += 1
    # 부감독관 계산
    if temp > 0:
        if temp % C:
            ans += (temp // C + 1)
        else:
            ans += (temp // C)
    total_ans += ans
print(total_ans)