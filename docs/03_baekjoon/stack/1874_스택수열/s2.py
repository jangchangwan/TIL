# 1874_스택_수열_문제풀이
# 2022-02-23
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
stack = list()
answer = list()
# 오름차순이므로 굳이 리스트 안만들어도 됨
i = 1
for n in range(N):
    num = int(input())
    while num >= i:
        stack.append(i)
        answer.append("+")
        # 1씩 더해준다
        i += 1
    # Top 과 num 랑 동일할 경우
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    # 안맞을 경우
    else:
        answer = ["NO"]
        break

for ans in answer:
    print(ans)