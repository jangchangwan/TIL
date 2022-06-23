# 1717_집합의 표현
# 2022-05-18
# 345924 KB / 564 ms
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
# 최대 재귀 깊이 변경
'''
설정없이 할 경우 기본적으로 파이썬 최대 재귀횟수는 1000으로 설정되어있으므로
68% 에서 RecursionError가 발생한다.
이를 해결하기위해 사용
깊이를 너무 높은 값을 줄경우 메모리 초과 에러 발생
추천 기본값이 10**9라서 줄여가며 확인헀습니다.
10**6일 경우 시간 초과 발생
10**4일 경우 RecursionError 발생
'''
sys.setrecursionlimit(10**5)


# 특정 원소가 속한 집합을 찾기
def find_parent(x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        # 특정 원소의 값을 루트 원소 값으로 변경하고
        # 그 값을 리턴하니
        # 시간이 확 줄어들었다
        parent[x] = find_parent(parent[x])
        return parent[x]
    return x


# 두 원소가 속한 집합을 합치기
def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


# 입력
N, M = map(int, input().split())
# 리스트로 할경우 조회시 시간초과가 발생하는거 같아
# 딕셔너리로 변경 후 값 넣어주기
# 하지만 똑같이 시간초과 발생
parent = {}
for i in range(N+1):
    parent[i] = i

# M 만큼 반복
for _ in range(M):
    # 입력
    operation, a, b = map(int, input().split())
    # 출력 operation
    if operation:
        # 루트 노드가 같을 경우
        # 같은 집합 내에 있다는 얘기
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
    # 입력 operation
    else:
        union_parent(a, b)