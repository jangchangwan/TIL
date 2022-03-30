# 1107_리모콘_문제풀이
# 2022-03-30
# EOFError
import sys
sys.stdin = open('input.txt', 'r')


start_num = 100

end_num = int(input())
M = int(input())
button = list(map(int, input().split()))

cnt = abs(start_num - end_num)
for i in range(1000001):
    temp = str(i)
    state = False

    for j in temp:
        if int(j) in button:
            state = True
            break
        elif state:
            continue

    else:
        cnt = min(cnt, abs(end_num-i) + len(str(i)))

print(cnt)