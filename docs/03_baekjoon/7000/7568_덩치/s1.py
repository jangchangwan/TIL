# 7568_덩치_문제풀이
# 2022-02-27
import sys
sys.stdin = open('input.txt', 'r')

# 사람수
N = int(input())
N_lst = list()
# 사람 몸무게와 키
for i in range(1, N+1):
    kg, cm = map(int, input().split())
    N_lst.append((kg, cm, i))

res = []
for i in N_lst:
    ans = 1
    for j in N_lst:
        if i[0] < j[0] and i[1] < j[1]:
            ans += 1
    res.append(ans)
print(*res)