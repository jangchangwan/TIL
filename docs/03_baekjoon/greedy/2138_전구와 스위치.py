""" 문제
i 번 스위치를 누르면 i-1, i, i+1 스위치가 상태변환

처음을 누르는 경우와 안누른 경우를 나눠서 체크한다
"""
import sys

def change_zero(light):
    count = 1
    light[0] = not light[0]
    light[1] = not light[1]

    for i in range(1, len(light)):
        if light[i-1] == target[i-1]:
            continue
        else:
            count += 1

            light[i-1] = not light[i-1]
            light[i] = not light[i]

            if i < len(light)-1:
                light[i+1] = not light[i+1]

    if target == light:
        return count
    return 987654321

def non_change_zero(light):
    count = 0

    for i in range(1, len(light)):
        if light[i-1] == target[i-1]:
            continue
        else:
            count += 1

            light[i-1] = not light[i-1]
            light[i] = not light[i]

            if i < len(light)-1:
                light[i+1] = not light[i+1]

    if target == light:
        return count

    return 987654321

N = int(input())

now = list(map(int, sys.stdin.readline().rstrip("\n")))
target = list(map(int, sys.stdin.readline().rstrip("\n")))

result = min(change_zero(now[:]), non_change_zero(now[:]))
if result == 987654321:
    print(-1)
else:
    print(result)