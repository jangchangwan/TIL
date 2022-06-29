# 1744_수 묶기
# 2022-06-29
# 그리드(?)

N = int(input())
minus = []
plus = []
answer = 0
for _ in range(N):
    number = int(input())
    if number == 1:
        answer += 1
    elif number > 1:
        plus.append(number)
    else:
        minus.append(number)

minus.sort()
plus.sort(reverse= True)
M = len(minus)
P = len(plus)

if P % 2: # 홀수 인경우
    for i in range(0, len(plus)-1, 2):
        answer += plus[i] * plus[i+1]
    answer += plus[P-1]
else: # 짝수인 경우
    for i in range(0, len(plus),2):
        answer += plus[i] * plus[i+1]

if M % 2: # 홀수 인경우
    for i in range(0, len(minus) - 1, 2):
        answer += minus[i] * minus[i + 1]
    answer += minus[M - 1]
else:  # 짝수인 경우
    for i in range(0, len(minus), 2):
        answer += minus[i] * minus[i + 1]

print(answer)