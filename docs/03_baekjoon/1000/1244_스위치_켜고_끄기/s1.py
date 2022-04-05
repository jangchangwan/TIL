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
switch_list = [2]+list(map(int, input().split()))
T = int(input())


for i in range(T):
    gender, num = map(int, input().split())

    if gender == 1:
        i = 1
        while num < N:
            my_change(num)
            num *= i
            i += 1

    else:
        j = 1
        my_change(num)
        while num-j >= 0 and num+j <= N:
            if switch_list[num-j] == switch_list[num+j]:
                my_change(num - j)
                my_change(num + j)
                j += 1
            else:
                break

print(switch_list)