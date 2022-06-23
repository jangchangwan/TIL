# 14888_연산자_끼워놓기_문제풀이
# 2022-04-01

# 숫자와 연산자리스트를 순서가 있는 비복원 배열을 모두 만든다음
# 다 돌려서 값을 구한다.
# 시간초과 포기
import sys
sys.stdin = open('input.txt', 'r')


# 순서가 있는 비복원 추출
def order(n, picked, toPick):
    global temp
    if toPick == 0:
        temp.append(picked[:])
        return

    for i in range(n):
        if i not in picked:
            picked.append(i)
            order(n, picked, toPick - 1)
            picked.pop()





N = int(input())

num_lst = list(map(int, input().split()))
oper_lst = list(map(int, input().split()))
new_operation = []

for i in range(len(oper_lst)):
    temp = [i] * oper_lst[i]
    new_operation.extend(temp)
M = len(new_operation)
max_ans = -1000000000
min_ans = 1000000000

temp = []
order(N, [], N)
num_index = []
# 얕은 복사(?) 때문에 안에 숫자가 바뀌는걸 방지
for i in temp:
    num_index.append(i[:])

temp = []
oper_index = []
order(M, [], M)
for i in temp:
    oper_index.append(i[:])

for num in num_index:
    for oper in oper_index:
        temp = num_lst[:]

        for i in range(N-1):
            # 더하기

            if new_operation[oper[i]] == 0:
                temp[num[i+1]] = temp[num[i]] + temp[num[i+1]]
            # 빼기
            elif new_operation[oper[i]] == 1:
                temp[num[i]] = temp[num[i]] - temp[num[i+1]]
            # 곱하기
            elif new_operation[oper[i]] == 2:
                temp[num[i+1]] = temp[num[i]] * temp[num[i+1]]
            # 나누기
            elif new_operation[oper[i]] == 3:
                temp[num[i+1]] = temp[num[i]] // temp[num[i+1]]

        res = temp[num[-1]]
        min_ans = min(min_ans, res)
        max_ans = max(max_ans, res)

print(max_ans)
print(min_ans)
