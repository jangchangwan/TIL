# 1620_나는야_포켓몬_마스터_이다솜_문제풀이
# 2022-03-30

import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().rstrip().split())

pkm_dic = {}
reversed_dic = {}
for i in range(1, N+1):
    data = sys.stdin.readline().rstrip()
    pkm_dic[i] = data
    reversed_dic[data] = i


for m in range(M):
    command = sys.stdin.readline().rstrip()
    # 숫자입력시
    if command.isdigit():
        print(pkm_dic[int(command)])
    # 문자입력시
    else:
        print(reversed_dic[command])
