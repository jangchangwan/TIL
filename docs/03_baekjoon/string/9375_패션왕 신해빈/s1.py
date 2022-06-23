# 9375_패션왕 신해빈_문제풀이
# 2022-05-20

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())

    dress_dic = {}
    for _ in range(N):
        name, category = map(str, input().split())
        if category in dress_dic:
            dress_dic[category].append(name)
        else:
            dress_dic[category] = [name]

    cnt = 1

    for k in dress_dic:
        cnt *= (len(dress_dic[k]) + 1)

    print(cnt - 1)