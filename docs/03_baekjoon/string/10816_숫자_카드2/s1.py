# 10816_숫자_카드2_문제풀이
# 2022-04-05
import sys
sys.stdin = open('input.txt', 'r')

# 가지고있는 숫자
N = int(input())
N_lst = list(map(int, input().split()))
N_lst.sort()
# 찾고싶은 숫자
M = int(input())
M_lst = list(map(int, input().split()))


num_dic = {}
for n in N_lst:
    if n in num_dic:
        num_dic[n] += 1
    # 없을 경우 생성
    else:
        num_dic[n] = 1

res = []
for m in M_lst:
    if m in num_dic:
        res.append(num_dic[m])
    else:
        res.append(0)

print(*res)
