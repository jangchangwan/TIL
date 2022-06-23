# 14425_문자열 집합_문제풀이
# 2022-05-02

import sys
sys.stdin = open('input.txt', 'r')


def trie_insert(word):
    now = Trie
    for w in word:
        if w not in now:
            now[w] = dict()
        now = now[w]
    now['*'] = '*'


def search(word):
    now = Trie
    for w in word:
        if w not in now:
            return False
        now = now[w]
    # 별마킹이 있는지 확인
    if '*' in now:
        return True
    return False


N, M = map(int, input().split())

N_lst = list(input() for _ in range(N))
M_lst = list(input() for _ in range(M))

Trie = dict()

# 생성
for word in N_lst:
    trie_insert(word)

cnt = 0
# Search
for M in M_lst:
    if search(M):
       cnt += 1

print(cnt)




