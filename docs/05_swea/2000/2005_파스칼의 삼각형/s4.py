# 2005_파스칼의_삼각형 풀이
# 2022-02-21

# 파일 불러오기
import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스
T = int(input())
for t in range(1, T + 1):

    # N : 자연수
    N = int(input())
    ans = []
    for i in range(N):
        row = [1]
        for j in range(i):
            stack = [0] + row + [0]
            row = []
            right = stack.pop()
            for i in range(N):
                if stack == []:
                    break
                left = stack.pop()
                row.append(left + right)
                right = left
        ans.append(row)
    print('#{}'.format(t))
    for ans_row in ans:
        print(*ans_row)