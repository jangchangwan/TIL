# 17219_비밀번호_찾기_문제풀이
# 2022-03-30

import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

password_dic = {}

for _ in range(N):
    address, password = map(str, input().split())
    password_dic[address] = password

for _ in range(M):
    find_address = input()
    print(password_dic[find_address])