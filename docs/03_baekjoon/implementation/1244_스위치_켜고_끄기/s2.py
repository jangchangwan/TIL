# 남 학생은 받은 숫자의 배수의 상태를 바꾼다
# 여 학생은 양옆중 좌우대칭인 부분까지 바꾼다
import sys
sys.stdin = open('input.txt', 'r')


# 1 0 스위칭 함수
def my_change(n):
    if switch_list[n] == 1:
        switch_list[n] = 0
    else:
        switch_list[n] = 1


N = int(input())
switch_list = [2] + list(map(int, input().split()))
T = int(input())


for t in range(T):
    gender, num = map(int, input().split())
    # 남자
    if gender == 1:
        for i in range(num, N+1, num):
            my_change(i)

    # 여자
    else:
        my_change(num)
        for j in range(N//2):
            if num + j > N or num - j < 1:
                break
            if switch_list[num-j] == switch_list[num+j]:
                my_change(num - j)
                my_change(num + j)
            else:
                break
for i in range(1, N+1):
    print(switch_list[i], end=' ')
    if i % 20 == 0:
        print()

