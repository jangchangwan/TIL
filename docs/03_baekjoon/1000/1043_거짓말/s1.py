# 1043 거짓말 문제풀이
# 2022-05-20


import sys
sys.stdin = open('input.txt', 'r')

# 특정 원소가 속한 집합을 찾기
def find_parent(x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
        return parent[x]
    return x


# 두 원소가 속한 집합을 합치기
def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    # value값을 진실을 아는사람으로 변경한다
    if pa in truth:
        parent[pb] = pa
    elif pb in truth:
        parent[pa] = pb
    # 없을경우 루트 값
    else:
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb


# N : 사람 , M : 파티 수
N, M = map(int, input().split())
truth = list(map(int, input().split()))[1:]

# 집합 만들기
parent = {}
for i in range(N+1):
    parent[i] = i

total_people = []
for _ in range(M):
    m_lst = list(map(int, input().split()))
    people = m_lst[1:]

    for idx in range(m_lst[0]-1):
        union_parent(people[idx], people[idx+1])
    total_people.append(people)

cnt = 0
for party in total_people:
    for i in party:
        if find_parent(i) in truth:
            break
    else:
        cnt += 1

print(cnt)